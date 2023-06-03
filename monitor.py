import psutil
import vonage
from dotenv import dotenv_values

config = dotenv_values(".env")

# the disk usage threshold in percentage form
threshold = 50

def get_message(value, device):
    return (
        f"Your Disk Usage is at {value} % on {device}. "
        "Delete some files soon to create disk space!"
    )


if __name__ == "__main__":
    client = vonage.Client(
        key=config["VONAGE_API_KEY"], secret=config["VONAGE_API_SECRET"]
    )

    # get disk usage stats
    stats = psutil.disk_usage("/")

    # device: can be any machine e.g server 1.89.200.4
    device = "local dev machine"

    # if disk usage is above given threshold, send out an sms alert
    if stats[-1] > threshold:

        client.sms.send_message(
            {
                "from": config["VONAGE_SENDER"],
                "to": config["RECIPIENT"],
                "text": f"{get_message(stats[-1], device)}",
            }
        )
