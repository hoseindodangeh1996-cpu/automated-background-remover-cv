from pathlib import Path
from rembg import remove, new_session
from PIL import Image

# Configuration
INPUT_FOLDER = Path("ax_input")
OUTPUT_FOLDER = Path("ax_utput")
FILE_NAME = "#e9d5ff.png"

source_path = INPUT_FOLDER / FILE_NAME
result_path = OUTPUT_FOLDER / "logo_transparent.png"


def process_logo_pipeline():
    print(f"Starting image processing for: {FILE_NAME}")

    if not source_path.exists():
        print(f"Error: Input file not found at {source_path}")
        return

    try:
        OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

        # Step 1: High-quality upscaling using Lanczos filter
        print("Upscaling image resolution to preserve edges...")
        with Image.open(source_path) as img:
            scale_factor = 3
            target_size = (int(img.width * scale_factor), int(img.height * scale_factor))
            enhanced_img = img.resize(target_size, Image.Resampling.LANCZOS)

            # Step 2: Background removal using high-precision model
            print("Applying AI background removal model...")
            bg_session = new_session("isnet-general-use")
            final_output = remove(enhanced_img, session=bg_session)

            # Step 3: Saving the clean PNG file
            final_output.save(result_path, "PNG")

        print(f"Process completed successfully! Output saved to: {result_path}")

    except Exception as error:
        print(f"An error occurred during processing: {error}")


if __name__ == "__main__":
    process_logo_pipeline()