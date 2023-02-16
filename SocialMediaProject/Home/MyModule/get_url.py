from cloudinary.utils import cloudinary_url

def get_post_url(my_object):

    if my_object.image:
        public_id = my_object.image.public_id

        # Generate a URL for the image using the public ID and any desired transformation options
        url, options = cloudinary_url(public_id, width=400, crop="fill")
        print(url)
        return url
    return None

def get_user_url(my_object):
    if my_object.profile_image:
        public_id = my_object.profile_image.public_id

        # Generate a URL for the image using the public ID and any desired transformation options
        url, options = cloudinary_url(public_id, width=400, crop="fill")
        print(url)
        return url
    return None