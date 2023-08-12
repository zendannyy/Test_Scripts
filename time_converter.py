import argparse
import time
from datetime import datetime
import pytz

def unix_to_utc(stmp):
    """
    Convert a local timestamp to UTC.
    Args:
    - local_timestamp (str): The local timestamp in 'YYYY-MM-DD HH:MM:SS' format.
    Returns:
    - str: The UTC timestamp.
    """
    converted_ts = time.strftime("%m-%d-%Y %H:%M:%S", time.localtime(stmp))
    return converted_ts


def local_to_utc(smtp, timezone):
    # local_ts = datetime.strptime(smtp, '%Y-%m-%d %H:%M:%S')
    local_ts = datetime.fromtimestamp(smtp, pytz.timezone(timezone))
    # local_dt = local_tz.localize(local_ts)
    utc_ts = local_ts.astimezone(pytz.utc)
    return utc_ts.strftime('%Y-%m-%d %H:%M:%S')


def main():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="""Supply the timestamp you want to convert. Will print human readable timestamps.
        usage: test_converter.py [-h] [-t TIMESTAMP] """)
    parser.add_argument('-t', '--timestamp', type=int, required=True, help='Converts the timestamp supplied at the cli to UTC')
    parser.add_argument('-z', '--timezone', type=str, required=True, default='UTC', help='Timezone of the timestamp supplied. Default is UTC.')
    parser.add_argument('-f', '--file', required=False, help='Formats the file given')
    args = parser.parse_args()
    
    if args.timestamp:
        print("UTC time for {} is {}".format(args.timestamp, unix_to_utc(args.timestamp)))
        print(type(args.timestamp))
    
    if args.timezone:
        local_to_utc(args.timestamp, args.timezone)

 
if __name__ == '__main__':
    main()

