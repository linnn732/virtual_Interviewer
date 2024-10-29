import sda, sys
import os
#os.environ["CUDA_VISIBLE_DEVICES"] = "3"
va = sda.VideoAnimator(model_path="timit")# Instantiate the animator
src_img = sys.argv[1]
src_audio = sys.argv[2]
output_name = sys.argv[3]
print(type(va))
vid, aud = va(src_img, src_audio)
va.save_video(vid, aud, output_name)
print("file saved: %s"% output_name)
