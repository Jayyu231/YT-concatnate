from YT_concatnate.pipeline.steps.get_video_list import GetVideoList
from YT_concatnate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'CHANNEL_ID': CHANNEL_ID

    }
    steps = [
        GetVideoList()
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()





