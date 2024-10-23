import os
import flet as ft
from .convert import convert_images_to_pdf

def main(page: ft.Page):
    page.title = "Image to PDF Converter"

    selected_images = []

    def on_file_picker_result(e: ft.FilePickerResultEvent):
        if e.files:
            selected_images.clear()
            for file in e.files:
                selected_images.append(file.path)
            selected_files.value = "\n".join([file.name for file in e.files])
        else:
            selected_files.value = "No files selected."
        page.update()

    def on_convert_click(e):
        pdf_dir = output_dir.value
        title = pdf_title.value

        if not selected_images:
            result.value = "No images selected."
            page.update()
            return

        if not os.path.exists(pdf_dir):
            os.makedirs(pdf_dir)

        try:
            output_pdf = convert_images_to_pdf(selected_images, pdf_dir, title)
            result.value = f"PDF created successfully: {output_pdf}"
        except Exception as ex:
            result.value = f"Error: {str(ex)}"

        page.update()

    file_picker = ft.FilePicker(on_result=on_file_picker_result)
    page.overlay.append(file_picker)

    select_files_button = ft.ElevatedButton(
        text="Select Images",
        on_click=lambda _: file_picker.pick_files(file_type=["image/jpeg", "image/png"], allow_multiple=True)
    )
    selected_files = ft.Text(value="No files selected.")
    output_dir = ft.TextField(label="Output PDF Directory", value="data")
    pdf_title = ft.TextField(label="PDF Title", value="outputFileName")
    convert_button = ft.ElevatedButton(text="Convert to PDF", on_click=on_convert_click)
    result = ft.Text()

    page.add(
        ft.Column(
            [
                ft.Text(value="Image to PDF Converter", size=24, color=ft.colors.BLUE_900),
                select_files_button,
                selected_files,
                output_dir,
                pdf_title,
                convert_button,
                result
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)