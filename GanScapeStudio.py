# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template, request
import torch as th
from pro_gan_pytorch import PRO_GAN as pg
import torchvision.utils as vutils
import random

# Create the application object
app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def home_page(): 

    return render_template('index.html')  # render a template


@app.route('/updatedisplay',methods=["POST"])
def generateNewImages():
    
    print("Generate image")
    device = th.device("cuda" if th.cuda.is_available() else "cpu")

    gen = th.nn.DataParallel(pg.Generator(depth=6,latent_size=128))

    gen.load_state_dict(th.load("GAN_GEN_5.pth", map_location=str(device)))
#     noise = th.randn(1, 128).to(device)
#     sample_image = gen(noise, depth=5, alpha=1).detach()
#     vutils.save_image(sample_image[0, :, :, :], 'portrait_' + str(1) + '.png'.format(3))
    noise = th.randn(32, 128).to(device)
    sample_image = gen(noise, depth=5, alpha=1).detach()
    
    for x in range(18):
        
        vutils.save_image(sample_image[x,:,:,:], '/home/ubuntu/GanZoo/static/img/display/portrait_' + str(x) + '.png'.format(3),normalize=True)
    return render_template('index.html') 


    
@app.route('/output')
def tag_output():
#       
       # Pull input
       some_input =request.args.get('user_input')            
       
       # Case if empty
       if some_input == '':
           return render_template("index.html",
                                  my_input = some_input,
                                  my_form_result="Empty")
       else:
           some_output="yeay!"
           some_number=3
           some_image="giphy.gif"
           return render_template("index.html",
                              my_input=some_input,
                              my_output=some_output,
                              my_number=some_number,
                              my_img_name=some_image,
                              my_form_result="NotEmpty")

# No caching at all for API endpoints.
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

# start the server with the 'run()' method
if __name__ == "__main__":
   
#     app.run(debug=True)
    app.run(host="0.0.0.0", port=8501) #will run locally http://127.0.0.1:5000/

