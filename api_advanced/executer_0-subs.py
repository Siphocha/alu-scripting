import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').num_of_subs
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))