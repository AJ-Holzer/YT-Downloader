import flet as ft  # type:ignore[import-untyped]

from env.classes.downloader import VideoDownloader


def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        folder: str = str(e.path)
        url: str = str(url_input.value).strip()

        if not folder:
            feedback.value = "Please provide a folder where to store the file!"
            feedback.color = "red"
            feedback.update()
            return
        elif not url:
            feedback.value = "Provide an URL!"
            feedback.color = "red"
            feedback.update()
            return

        try:
            feedback.value = "Downloading..."
            feedback.color = "green"
            feedback.update()

            print(f"Downloading to '{folder}'...")
            downloader: VideoDownloader = VideoDownloader(download_path=folder)
            downloader.download(url=str(url_input.value))

            feedback.value = "Download completed!"
            feedback.update()
        except Exception as ex:
            print(f"Exception has occurred while downloading: {ex}")
            feedback.value = f"Error: {ex}"
            feedback.color = "red"
            feedback.update()

    url_input = ft.TextField(label="YouTube Video URL", multiline=True)
    feedback = ft.Text(value="", color="green")

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)

    download_btn: ft.ElevatedButton = ft.ElevatedButton(
        "Download",
        on_click=lambda _: pick_files_dialog.get_directory_path(
            dialog_title="Select where the video should be stored."
        ),
    )

    page.add(
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Column(
                        [
                            url_input,
                            download_btn,
                            feedback,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True,
                    ),
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=40,
            alignment=ft.alignment.center,
            expand=True,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)  # type:ignore
