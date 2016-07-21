import os
import matplotlib.pyplot as plt

from gamma import *

BASEDIR = "/Users/rzinkstok/Desktop/dvhs/"


def read_dvh(p):
    with open(p, "r") as fp:
        lines = fp.readlines()

    name = lines[0].split(":")[1].strip()
    volume = float(lines[1].split(":")[1]) 
    xs, ys = zip(*[[float(x) for x in l.split()] for l in lines[2:]])
    return name, volume, xs, ys


for d in os.listdir(BASEDIR):
    patpath = os.path.join(BASEDIR, d)
    if not os.path.isdir(patpath):
        continue
    print patpath
    i = 0

    with open(os.path.join(patpath, "results.txt"), "w") as fp:
        while True:
            dcm_dvh_path = os.path.join(patpath, "dcm_{0:02}.dat".format(i))
            p3_dvh_path = os.path.join(patpath, "p3_{0:02}.dat".format(i))
            if not os.path.exists(dcm_dvh_path) or not os.path.exists(p3_dvh_path):
                break

            dcm_name, dcm_volume, dcm_xs, dcm_ys = read_dvh(dcm_dvh_path)
            p3_name, p3_volume, p3_xs, p3_ys = read_dvh(p3_dvh_path)
            fp.write("Name: {0}\n".format(dcm_name))
            print "Name: {0} / {1}".format(dcm_name, p3_name)
            fp.write("Volume Pinnacle: {0} cc\n".format(p3_volume))
            fp.write("Volume RTSTRUCT: {0} cc\n".format(dcm_volume))
            print "Volume: {0} / {1}".format(dcm_volume, p3_volume)

            voldev = 100*(dcm_volume-p3_volume)/p3_volume
            fp.write("Volume deviation: {0}%\n".format(voldev))
            print "Volume deviation: {0}%".format(voldev)
            
            
            g_xs, g_ys = full_gamma(dcm_xs, dcm_ys, p3_xs, p3_ys, 0.05, 0.01)
            gamma_pass = 100*numpy.sum(numpy.array(g_ys)<=1.0)/float(len(g_ys))
            fp.write("Gamma passing: {0}%\n".format(gamma_pass))
            print "Passing: {0}%".format(gamma_pass)
            fp.write("\n")
        
            plt.plot(p3_xs, p3_ys, "r", dcm_xs, dcm_ys, "b", g_xs, g_ys, "g")
            axes = plt.gca()
            axes.set_ylim([0,1.1])
            plt.savefig(os.path.join(patpath, "{0}.pdf".format(dcm_name)))
            i+=1

