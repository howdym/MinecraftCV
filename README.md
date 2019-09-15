# MinecraftCV

# IMPORTANT: The main feature of this code, which is using computer vision for feature detection, IS NOT WRITTEN BY ME. 

# SOURCE: NOT MEANT FOR PROMOTION OR ENDORSEMENT, BUT JUST TO CITE THE SOURCE CODE: 
https://github.com/abidrahmank/OpenCV2-Python-Tutorials/blob/master/source/py_tutorials/py_feature2d/py_orb/py_orb.rst </br>
https://github.com/abidrahmank/OpenCV2-Python-Tutorials/blob/master/source/py_tutorials/py_feature2d/py_matcher/py_matcher.rst

His code can be found in the "analyze.py" file. 

# Purpose
This is a script that looks through a video and detects when a player uses MakeCode in Minecraft. It returns the timestamps of which a player uses MakeCode or the Inventory. 

# Features 
**image_processing.py:** contains all the functions related to processing an image out of a video </br>
**mass_processing.py:** automates the running of this script on every set of data stored in our lab computer </br>
**video_processing.py:** looks through a video and detects when a player uses MakeCode in Minecraft </br>
**frames:** folder that holds the images that are processed in the process of checking the video </br>
**target.png:** containing an image of the MakeCode page, which is used for feature detection </br>
**testing.py:** script that helps with testing the code </br>
**testing:** folder holding test images used </br>

# Future iterations 
Will include feature where script detects when a player uses the Inventory or Chest in Minecraft.

#

Copyright (C) 2000-2019, Intel Corporation, all rights reserved. </br>
Copyright (C) 2009-2011, Willow Garage Inc., all rights reserved. </br>
Copyright (C) 2009-2016, NVIDIA Corporation, all rights reserved. </br>
Copyright (C) 2010-2013, Advanced Micro Devices, Inc., all rights reserved. </br>
Copyright (C) 2015-2016, OpenCV Foundation, all rights reserved. </br>
Copyright (C) 2015-2016, Itseez Inc., all rights reserved. </br>
Third party copyrights are property of their respective owners. </br>

This software is provided by the copyright holders and contributors “as is” and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. In no event shall copyright holders or contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.