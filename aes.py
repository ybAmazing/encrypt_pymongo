from Crypto.Cipher import AES
import bson
from bson.binary import Binary, UUIDLegacy
from pymongo import config

key = config.key

obj = AES.new(key)

def encrypt_helper(s):
	length = 16 - (len(s) % 16)
	s += chr(length) * length
	s = obj.encrypt(s)
	s = Binary(s, 1)
	return s

def decrypt_helper(s):
	s = obj.decrypt(s)
	buf = bytearray(s)
	length = buf[-1]
	s = s[: -length]
	return s

def encrypt_doc(doc):
	if isinstance(doc, str):
		return encrypt_helper(doc)
	if isinstance(doc, dict):
		for key in doc:
			if cmp(key, "channel") != 0:
				doc[key] = encrypt_doc(doc[key])
		return doc

	if isinstance(doc, list):
		for i in range(len(doc)):
			doc[i] = encrypt_doc(doc[i])
		return doc
	return doc


def decrypt_doc(doc):
	if isinstance(doc, Binary):
		return decrypt_helper(doc)
	if isinstance(doc, dict):
		temp_doc = {}
		for key in doc:
			#version 1
			#doc[key] = decrypt_doc(doc[key])

			#version 2
			temp_doc[str(key)] = decrypt_doc(doc[key])
		doc = temp_doc
		return doc

	if isinstance(doc, list):
		for i in range(len(doc)):
			doc[i] = decrypt_doc(doc[i])
		return doc
	return doc

