from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.metrics import dp
from kivy.core.window import Window
from PIL import Image
import os

# Try to import OCR libraries
try:
    import pytesseract
    USE_TESSERACT = True
except:
    USE_TESSERACT = False
    # Fallback: We'll use basic text extraction
    print("Tesseract not available, using fallback mode")

Window.clearcolor = (0.96, 0.96, 0.98, 1)


class TextExtractorApp(App):
    def build(self):
        self.title = "Text Extractor"
        self.selected_files = []
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        # Header
        header = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(120), spacing=dp(5))
        
        title_label = Label(
            text='📸 Image Text Extractor',
            font_size=dp(28),
            bold=True,
            color=(0.17, 0.24, 0.31, 1),
            size_hint_y=None,
            height=dp(50)
        )
        
        subtitle_label = Label(
            text='Extract text from images instantly',
            font_size=dp(14),
            color=(0.5, 0.55, 0.55, 1),
            size_hint_y=None,
            height=dp(30)
        )
        
        header.add_widget(title_label)
        header.add_widget(subtitle_label)
        
        # File info label
        self.file_label = Label(
            text='No images selected',
            font_size=dp(12),
            color=(0.58, 0.62, 0.62, 1),
            size_hint_y=None,
            height=dp(30)
        )
        
        # Buttons layout
        button_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(220), spacing=dp(10))
        
        # Select button
        select_btn = Button(
            text='📁 Select Images',
            font_size=dp(16),
            bold=True,
            background_color=(0.2, 0.6, 0.86, 1),
            background_normal='',
            size_hint_y=None,
            height=dp(50)
        )
        select_btn.bind(on_press=self.select_images)
        
        # Copy button
        copy_btn = Button(
            text='📋 Copy Text',
            font_size=dp(16),
            background_color=(0.18, 0.8, 0.44, 1),
            background_normal='',
            size_hint_y=None,
            height=dp(50)
        )
        copy_btn.bind(on_press=self.copy_text)
        
        # Save button
        save_btn = Button(
            text='💾 Save to File',
            font_size=dp(16),
            background_color=(0.9, 0.49, 0.13, 1),
            background_normal='',
            size_hint_y=None,
            height=dp(50)
        )
        save_btn.bind(on_press=self.save_text)
        
        # Clear button
        clear_btn = Button(
            text='🗑️ Clear',
            font_size=dp(16),
            background_color=(0.58, 0.65, 0.65, 1),
            background_normal='',
            size_hint_y=None,
            height=dp(50)
        )
        clear_btn.bind(on_press=self.clear_text)
        
        button_layout.add_widget(select_btn)
        button_layout.add_widget(copy_btn)
        button_layout.add_widget(save_btn)
        button_layout.add_widget(clear_btn)
        
        # Text area label
        text_label = Label(
            text='Extracted Text',
            font_size=dp(16),
            bold=True,
            color=(0.17, 0.24, 0.31, 1),
            size_hint_y=None,
            height=dp(35),
            halign='left',
            valign='middle'
        )
        text_label.bind(size=text_label.setter('text_size'))
        
        # Scrollable text area
        scroll_view = ScrollView(do_scroll_x=False)
        
        self.text_area = TextInput(
            text='',
            multiline=True,
            readonly=False,
            background_color=(0.98, 0.98, 0.98, 1),
            foreground_color=(0.17, 0.24, 0.31, 1),
            font_size=dp(14),
            padding=[dp(15), dp(15)]
        )
        
        scroll_view.add_widget(self.text_area)
        
        # Status bar
        self.status_label = Label(
            text='Ready to extract text',
            font_size=dp(12),
            color=(0.93, 0.94, 0.95, 1),
            size_hint_y=None,
            height=dp(40),
            canvas={'color': (0.2, 0.29, 0.37, 1)}
        )
        
        # Add all widgets to main layout
        main_layout.add_widget(header)
        main_layout.add_widget(self.file_label)
        main_layout.add_widget(button_layout)
        main_layout.add_widget(text_label)
        main_layout.add_widget(scroll_view)
        main_layout.add_widget(self.status_label)
        
        return main_layout
    
    def select_images(self, instance):
        """Open file chooser to select images"""
        content = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10))
        
        filechooser = FileChooserIconView(
            filters=['*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif', '*.tiff', '*.tif'],
            multiselect=True
        )
        
        button_box = BoxLayout(size_hint_y=None, height=dp(50), spacing=dp(10))
        
        select_btn = Button(text='Select', background_color=(0.2, 0.6, 0.86, 1), background_normal='')
        cancel_btn = Button(text='Cancel', background_color=(0.58, 0.65, 0.65, 1), background_normal='')
        
        button_box.add_widget(select_btn)
        button_box.add_widget(cancel_btn)
        
        content.add_widget(filechooser)
        content.add_widget(button_box)
        
        popup = Popup(title='Select Images', content=content, size_hint=(0.9, 0.9))
        
        def on_select(btn):
            self.selected_files = filechooser.selection
            if self.selected_files:
                self.file_label.text = f'Selected: {len(self.selected_files)} image(s)'
                self.extract_text_from_images()
            popup.dismiss()
        
        def on_cancel(btn):
            popup.dismiss()
        
        select_btn.bind(on_press=on_select)
        cancel_btn.bind(on_press=on_cancel)
        
        popup.open()
    
    def extract_text_from_images(self):
        """Extract text from selected images"""
        if not self.selected_files:
            self.status_label.text = 'No images selected'
            return
        
        try:
            total = len(self.selected_files)
            self.text_area.text = ''
            
            for idx, image_path in enumerate(self.selected_files, 1):
                self.status_label.text = f'Extracting text... ({idx}/{total})'
                
                # Open and extract text
                image = Image.open(image_path)
                
                if USE_TESSERACT:
                    extracted_text = pytesseract.image_to_string(image)
                else:
                    # Fallback message for Android without Tesseract
                    extracted_text = f"Image: {os.path.basename(image_path)}\n[OCR extraction requires setup]\n\nFor full OCR on Android, use the web app version."
                
                # Add to text area
                separator = f"\n{'='*60}\n"
                header = f"IMAGE {idx}: {os.path.basename(image_path)}\n{separator}"
                
                self.text_area.text += header + extracted_text + "\n"
            
            self.status_label.text = f'Successfully extracted text from {total} image(s)!'
            
        except Exception as e:
            self.status_label.text = f'Error: {str(e)}'
            self.show_popup('Error', f'Failed to extract text:\n{str(e)}')
    
    def copy_text(self, instance):
        """Copy text to clipboard"""
        if self.text_area.text.strip():
            Clipboard.copy(self.text_area.text)
            self.status_label.text = 'Text copied to clipboard!'
            self.show_popup('Success', 'Text copied to clipboard!\nYou can now paste it anywhere.')
        else:
            self.show_popup('Warning', 'No text to copy!')
    
    def save_text(self, instance):
        """Save text to file"""
        if not self.text_area.text.strip():
            self.show_popup('Warning', 'No text to save!')
            return
        
        # Simple save dialog
        content = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10))
        
        filename_input = TextInput(
            text='extracted_text.txt',
            multiline=False,
            size_hint_y=None,
            height=dp(40),
            font_size=dp(14)
        )
        
        button_box = BoxLayout(size_hint_y=None, height=dp(50), spacing=dp(10))
        save_btn = Button(text='Save', background_color=(0.2, 0.6, 0.86, 1), background_normal='')
        cancel_btn = Button(text='Cancel', background_color=(0.58, 0.65, 0.65, 1), background_normal='')
        
        button_box.add_widget(save_btn)
        button_box.add_widget(cancel_btn)
        
        content.add_widget(Label(text='Enter filename:', size_hint_y=None, height=dp(30)))
        content.add_widget(filename_input)
        content.add_widget(button_box)
        
        popup = Popup(title='Save File', content=content, size_hint=(0.9, None), height=dp(250))
        
        def on_save(btn):
            try:
                filename = filename_input.text
                # Save to Downloads or Documents folder
                from android.storage import primary_external_storage_path
                downloads_path = os.path.join(primary_external_storage_path(), 'Download')
                filepath = os.path.join(downloads_path, filename)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(self.text_area.text)
                
                self.status_label.text = f'Saved to {filepath}'
                self.show_popup('Success', f'File saved to:\n{filepath}')
            except:
                # Fallback for desktop testing
                try:
                    with open(filename_input.text, 'w', encoding='utf-8') as f:
                        f.write(self.text_area.text)
                    self.status_label.text = f'Saved to {filename_input.text}'
                    self.show_popup('Success', f'File saved: {filename_input.text}')
                except Exception as e:
                    self.show_popup('Error', f'Failed to save:\n{str(e)}')
            popup.dismiss()
        
        save_btn.bind(on_press=on_save)
        cancel_btn.bind(on_press=lambda x: popup.dismiss())
        
        popup.open()
    
    def clear_text(self, instance):
        """Clear text area"""
        self.text_area.text = ''
        self.file_label.text = 'No images selected'
        self.selected_files = []
        self.status_label.text = 'Cleared'
    
    def show_popup(self, title, message):
        """Show a popup message"""
        content = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        content.add_widget(Label(text=message))
        
        close_btn = Button(
            text='OK',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.2, 0.6, 0.86, 1),
            background_normal=''
        )
        
        content.add_widget(close_btn)
        
        popup = Popup(title=title, content=content, size_hint=(0.8, None), height=dp(200))
        close_btn.bind(on_press=popup.dismiss)
        popup.open()


if __name__ == '__main__':
    TextExtractorApp().run()
