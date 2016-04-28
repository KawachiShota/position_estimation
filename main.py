import serial, time, math

import received_data
import normal_distribution_parameter
import normal_distribution_log_likelihood
#import normal_distribution_likelihood
import prior_distribution
import posterior_distribution
import normalization
import position_inference
import update


#instance
r_cal = received_data.Received_data()
pa_cal = normal_distribution_parameter.Normal_distribution_parameter()
l_cal = normal_distribution_log_likelihood.Normal_distribution_log_likelihood()
#l_cal = normal_distribution_likelihood.Normal_distribution_likelihood()
x_cal = prior_distribution.Prior_distribution()
y_cal = posterior_distribution.Posterior_distribution()
normal_cal = normalization.Normalization()
po_cal = position_inference.Position_inference()
ynew_cal = update.Update()

y_new_list = [0,1,2] #first posterior distribution(no mean)

while True:

    received_data1 = r_cal.received_data1()
    received_data2 = r_cal.received_data2()
    #received_data1 = -62.2
    #received_data2 = -58.7

    print "Data1=",received_data1
    print "Data2=",received_data2

    a_list = pa_cal.average_calculation()
    d_list = pa_cal.dispersion_calculation(a_list)
    #print "average=",a_list
    #print "dispersion=",d_list

    l_list = l_cal.likelihood(received_data1,received_data2,a_list,d_list)
    print "likelihood=",l_list

    l_normal_list = normal_cal.value_normalization(l_list)
    #print "l_normalization=",l_normal_list

    x_list = x_cal.prior_probability(y_new_list)
    #print "prior_probability=",x_list

    y_list = y_cal.posterior_probability(x_list,l_normal_list)
    #print "posterior_probability=",y_list

    y_normal_list = normal_cal.value_normalization(y_list)
    #print "y_normalization=",y_normal_list

    position = po_cal.y_judgement(y_normal_list)
    #print "position=",position

    y_new_list = ynew_cal.y_update(y_normal_list)
    #print y_new_list

    time.sleep(0.1)

