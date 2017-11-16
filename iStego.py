from PIL import Image
from functions import *
import argparse, sys, os
verbose = False
MAX_PROGRESS_BAR_LENGTH = 50

class InvalidFlag(Exception):
	'''Raised when user tries to encode and decode at the same time'''
	pass
class MessageTooLong(Exception):
	'''Raised if message can't fit in image'''
	pass

def encode(fileLoc, msg, output):
	if not os.path.isfile(fileLoc):
		raise InvalidFlag("ERROR! Input image does not exist!")
	verbosity("Opening and reading image")
	imge = Image.open(fileLoc)
	imge = imge.convert('RGB')
	width, height = imge.size
	verbosity("Image dimesions: {}x{}".format(width, height))
	
	hashtag_bin = "0100011"
	msg_bin = str2bin(msg) 
	if len(msg_bin + hashtag_bin) > (width * height):
		raise MessageTooLong("ERROR! Message too long to encode into image")
	verbosity("This is the message in binary: ")
	verbosity("print('" + msg_bin + "')")
	
	verbosity("Starting to encode message into image...")
	msg_bin = msg_bin + hashtag_bin
	count = 0
	null_byte = 8
	for i in range(height):
		for j in range(width):
			rgba = imge.getpixel((j, i))
			r = rgba[0]
			g = rgba[1]
			b = rgba[2]
			b_bin = str(int2bin(b))
			if count < len(msg_bin):
				b_bin = b_bin[:len(b_bin) - 1] + str(msg_bin[count])
				b = bin2int(b_bin)
				imge.putpixel((j, i), (r, g, b))
				count += 1
			else:
				if null_byte > 0:
					b_bin = b_bin[:len(b_bin) - 1] + "0"
					b = bin2int(b_bin)
					imge.putpixel((j, i), (r, g, b))
				else:
					break
		if null_byte < 1:
			break
		if verbose:
			progress_bar(cur=i, ttl=height, max_len=MAX_PROGRESS_BAR_LENGTH)
	if verbose:
		progress_bar(MAX_PROGRESS_BAR_LENGTH,MAX_PROGRESS_BAR_LENGTH,MAX_PROGRESS_BAR_LENGTH)
		print()
	verbosity("Saving image")
	imge.save(output)
	verbosity("Encoding COMPLETE! Image saved at %s" %output)
def decode(fileLoc, output=None):
	if not os.path.isfile(fileLoc):
		raise InvalidFlag("ERROR! Input image does not exist!")
	verbosity("Opening and reading image")
	imge = Image.open(fileLoc)
	width, height = imge.size
	verbosity("Image dimesions: {}x{}".format(width, height))
	
	msg_bin = ""
	msg = ""
	
	b_null_count = 0
	break_decode = False
	for i in range(height):
		for j in range(width):
			rgba = imge.getpixel((j, i))
			r = rgba[0]
			g = rgba[1]
			b = rgba[2]
			lsb = str(int2bin(b))[-1]
			msg_bin += lsb
			if lsb == "0":
				b_null_count += 1
			else:
				b_null_count = 0
			if b_null_count == 8:
				break_decode = True
				break
		if verbose:
			progress_bar(cur=i, ttl=height, max_len=MAX_PROGRESS_BAR_LENGTH)
		if break_decode: break
	if verbose:
		progress_bar(MAX_PROGRESS_BAR_LENGTH,MAX_PROGRESS_BAR_LENGTH,MAX_PROGRESS_BAR_LENGTH)
		print()
	
	verbosity("All trailing zeros will be stripped, this may mess up the last character")
	msg_bin = msg_bin.rstrip("0")
	verbosity("The retrieved message in binary:\n%s" %msg_bin)
	verbosity("Converting to string..")
	msg = bin2str(msg_bin)
	msg = msg[:-1]
	
	if output != None:
		verbosity("Writing message to file")
		with open(output, 'w') as otp:
			otp.write(msg)
	verbosity(msg)
def verbosity(*args):
	if verbose:
		for i in args:
			try:
				eval(i)
			except:
				print(i)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		prog="Image Steganographer",
		description="Simple Image Steganographer in Python3"
	)
	
	#Adds all positional arguments
	parser.add_argument("encode", nargs="?", help="Encode a message into an image")
	parser.add_argument("decode", nargs="?", help="Decode a message from a given image")
	
	#Adds all optional arguments
	parser.add_argument("--image", help="Location of image", dest="image")
	parser.add_argument("--output", help="Location to store output", dest="output")
	parser.add_argument("--message", help="Message to be encoded", dest="message")
	parser.add_argument("--verbose", help="Output debug information", dest="verbose", action="store_true")
	
	try:
		args = parser.parse_args()
		if args.encode and args.decode:
			raise InvalidFlag("ERROR! Cannot encode and decode simultaneously")
		elif not args.encode:
			raise InvalidFlag("ERROR! You must specify to either 'encode' or 'decode'")
		verbose = args.verbose
		if args.encode == "encode":
			if args.message == None or args.image == None or args.output == None:
				raise InvalidFlag("ERROR! Make sure your are using the --image/message/output flags")
			encode(fileLoc=args.image, msg=args.message, output=args.output)
		elif args.encode == "decode":
			if args.output == None:
				print("You did not specify an output text file, make sure to have verbose on to see output text")
			decode(fileLoc=args.image, output=args.output)
	except InvalidFlag as e:
		print(e)
		sys.exit(1)
	except MessageTooLong as e:
		print(e)
		sys.exit(1)