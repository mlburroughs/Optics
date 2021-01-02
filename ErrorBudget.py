'''

Error Budget
Description: This program computes error budget for optical systems


Author: Michelle Burroughs
Date 12/13/20

'''
import math


'''
Wavefront Error
'''

def wftotal_budget_rms(sigma_fitting, sigma_anisopl, sigma_temporal, sigma_meas, sigma_cali, sigma_tiptilt):
    wfsigma_total = math.sqrt((sigma_fitting^2) + (sigma_anisopl^2) + (sigma_temporal^2) + (sigma_meas^2) + (sigma_cali^2) + (sigma_tiptilt^2))
    return wfsigma_total


def pred_vs_meas(sigma_pred_array, sigma_meas_array):
    wfsigma_pred = wftotal_budget_rms(sigma_pred_array)
    wfsigma_meas = wftotal_budget_rms(sigma_meas_array)
    return wfsigma_pred, wfsigma_meas


# Wavefront error from using a guide star theta away from science target
def anisoplanatism_error(theta, theta_0):
    const = 5/3
    sigma_anisopl = math.sqrt((theta, theta_0)^const)
    return sigma_anisopl

# Wavefront error due to time lag
def temporal_error(tau, tau_0):
    const = 5/3
    sigma_temporal = math.sqrt(28,4*((tau/tau_0)^const))
    return sigma_temporal

# Accuracy of deformable mirror to remove wavefront aberrations
# u is .14 for segmented mirror with corrections, .28 for deformable mirror with continuous sheet
def fitting_error(d, r_0, u):
    const = 5/3
    sigma_fitting = math.sqrt(u*((d/r_0)^const))
    return sigma_fitting


