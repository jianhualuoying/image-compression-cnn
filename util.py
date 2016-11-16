import skimage.io
import skimage.transform
import numpy as np

def chunker(seq, size):
    # http://stackoverflow.com/a/25701576/1189865
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

def load_image(path):
    try:
        img = skimage.io.imread( path ).astype(np.float)
        img /= 255.0
        X = img.shape[0]
        Y = img.shape[1]
        S = min(X,Y)
        XX = int((X - S) / 2)
        YY = int((Y - S) / 2)
    except:
        return Exception("You need skimage to load the image")

    # if black and white image, repeat the channels
    if len(img.shape) == 2: img=np.tile(img[:,:,None], 3)
    return skimage.transform.resize( img[XX:XX+S, YY:YY+S], [224,224] )

def load_single_image(image):
    return np.expand_dims(load_image(image),0)

# def load_image_tensorflow(path):
#     img = skimage.io.imread( path ).astype( float )
#     img_resized = tf.image.resize_image_with_crop_or_pad(tf.convert_to_tensor(img, dtype=tf.float32), 224, 224)
#     img_resized = tf.expand_dims(img_resized, 0)
#     return img_resized, img
