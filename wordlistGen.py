import itertools as it
import argparse as ap
import progressbar as pb
from time import time, ctime

def confirmation(lenchars,minLen, maxLen):
    prevCount = 0
    prevSize = 0

    for ln in range(minLen, maxLen+1):
        prevCount += lenchars**ln
        prevSize += prevCount * ln

    mByte = prevSize / (1024**2)
    gByte = mByte / 1024
    tByte = gByte / 1024
    pByte = tByte / 1024

    print("Attention!")
    print("Size in MB: %.2f" % mByte)
    print("Size in GB: %.2f" % gByte)
    print("Size in TB: %.2f" % tByte)
    print("Size in PB: %.2f" % pByte)
    print("\nWordlistGen is about to generate a file with %i lines." % prevCount)

    while True:
        proceed = input('Are you sure you want to proceed? [Y]es  [N]o: ')
        if proceed.lower() == 'y' or proceed.lower() == 'yes':
            return True, prevCount
        elif proceed.lower() == 'n' or proceed.lower() == 'no':
            return False, _
        else:
            print('Please, type yes or no.')

def generator(chars,minLen,maxLen,prevCount):
    count = 0
    bar = pb.ProgressBar(max_value = prevCount)
    for length in range(minLen,maxLen+1):
        for perm in it.product(chars, repeat=length):
            outFile.write(''.join(perm)+'\n')
            count += 1
            bar.update(count)

if __name__ == "__main__":
    parser = ap.ArgumentParser(description='This tool generates wordlists from characters.')
    parser.add_argument('-c', '--chars', help='The characters to be used.', required=True)
    parser.add_argument('--min', help='The minimum word lenght.', required=True, type=int)
    parser.add_argument('--max', help='The maximum word lenght', required=True, type=int)
    parser.add_argument('-o', '--output', help='A file to save the wordlist.', required=True)
    args = parser.parse_args()

    try:
        outFile = open(args.output,'w')
    except Exception as e:
        raise e

    confirm, prevCount = confirmation(len(args.chars), args.min, args.max)

    if confirm:
        print("Initiating operation...")
        startTime = time()
        print("Start time: %s" % ctime(startTime))

        generator(args.chars,args.min,args.max,prevCount)

        endTime = time()
        print("Done.\nEnd time: %s" % ctime(endTime))
        print("Total operation time: %.2f seconds." % (float(endTime - startTime)))
        print("The file %s is ready to be used." % args.output)
    else:
        print('Aborting...')

