import logging
import sys
from pathlib import Path
from datetime import datetime

def setup_logger() -> logging.Logger:   
     # Define color codes
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

    # Create logs directory if it doesn't exist
    current_date = datetime.now().strftime('%Y-%m-%d')
    log_dir = Path('logs') / current_date
    log_dir.mkdir(parents=True, exist_ok=True)

    # Configure logging to both file and console
    log_file = log_dir / f'{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'

    # Configure logging with colors
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
        ]
    )
    
    if sys.stderr.isatty():
        logging.addLevelName(
            logging.INFO, 
            f"{GREEN}%s{RESET}" % logging.getLevelName(logging.INFO)
        )
        logging.addLevelName(
            logging.ERROR, 
            f"{RED}%s{RESET}" % logging.getLevelName(logging.ERROR)
        )
    
    logger = logging.getLogger(__name__)
    return logger

