from loguru import logger as lgr


def get_logger(file_name: str):
    lgr.add(
        file_name, 
        format="{time} {level} {message}", 
        level="DEBUG", 
        rotation="10 KB", 
        serialize=True
    )
    return lgr