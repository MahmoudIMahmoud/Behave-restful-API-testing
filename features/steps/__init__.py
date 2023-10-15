from behave_restful.lang import *
import pdb

@Step("debugging")
def debug_point(context):
    pdb.set_trace()
    print("================================","debug point","================================")
