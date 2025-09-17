import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        log_path = ".\\Logs\\automation.log"

        # Agar Logs folder exist nahi karta toh bana do
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        # Ek unique logger banate hain (default root logger se alag)
        logger = logging.getLogger("nopcommerce")
        logger.setLevel(logging.INFO)

        # Duplicate handlers avoid karne ke liye
        if not logger.handlers:
            # File handler
            file_handler = logging.FileHandler(log_path, mode="a")  # append mode
            formatter = logging.Formatter(
                '%(asctime)s: %(levelname)s: %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p'
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

            # Console handler (optional)
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        return logger

    def info(self, param):
        pass