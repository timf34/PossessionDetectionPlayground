from utils import *
from config import Config


def crop_single_player_images():
    # Initialize config
    config = Config()
    # Load image
    image = load_image(f"../{config.image_dir}/1.jpg")

    # Check if image has loaded correctly (not None)
    if image is None:
        print("Image not found")
        return

    # Crop blue player
    blue_player = crop_image(image, config.blue_player_bbox["x1"], config.blue_player_bbox["y1"],
                                config.blue_player_bbox["x2"] - config.blue_player_bbox["x1"],
                                config.blue_player_bbox["y2"] - config.blue_player_bbox["y1"])

    # Show blue player
    # cv2.imshow("Blue player", blue_player)
    # cv2.waitKey(0)

    # Crop white player
    white_player = crop_image(image, config.white_player_bbox["x1"], config.white_player_bbox["y1"],
                                config.white_player_bbox["x2"] - config.white_player_bbox["x1"],
                                config.white_player_bbox["y2"] - config.white_player_bbox["y1"])

    cv2.imshow("White player", white_player)
    cv2.waitKey(0)

    # Save blue player
    cv2.imwrite(f"../{config.image_dir}/blue_player.jpg", blue_player)
    # Save white player
    cv2.imwrite(f"../{config.image_dir}/white_player.jpg", white_player)


def main():
    crop_single_player_images()


if __name__ == "__main__":
    main()
