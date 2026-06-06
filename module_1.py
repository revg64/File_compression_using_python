import zlib,base64

def compress_file(inputfile,outputfile):
    #compressing file
    #compressed file can not be readed we have to decompress it

    #reading file
    data=open(inputfile,'r').read() #convert this string into bytes
    data_bytes=bytes(data,'utf-8')

    #encoding
    compressed_data=base64.b64encode(zlib.compress(data_bytes,9))#level of compression(0-9)

    #convet bytes to string
    decoded_data=compressed_data.decode('utf-8')

    #writing data to file
    compressed_file=open(outputfile,'w')
    compressed_file.write(decoded_data)
    #for compression we use zlib
    #for encoding we use base64

def decompress_file(inputfile,outputfile):
    file_content=open(inputfile,'r').read()
    encoded_data=file_content.encode('utf-8')
    decompressed_data=zlib.decompress(base64.b64decode(encoded_data)) # data is in bytes
    #decoding
    decoded_data=decompressed_data.decode('utf-8')
    file=open(outputfile,'w')
    file.write(decoded_data)
    file.close()