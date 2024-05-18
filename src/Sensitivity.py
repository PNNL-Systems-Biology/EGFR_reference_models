
import tellurium as te
import roadrunner

rr = roadrunner.RoadRunner()
# o = roadrunner.LoadSBMLOptions()
# rr.conservedMoietyAnalysis = False
rr.load('EGFR_5_HSW_MK-rev.xml')
# r = roadrunner.RoadRunner('EGFR_5_HSW_MK-rev.xml', o)
# print(rr.steadyState())
# rr.simulate(0, 700, 701)
# rr.plot()
# ccm = rr.getScaledConcentrationControlCoefficientMatrix()
# print(ccm)

# print('pEgfr_Lig')
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('Vr', rr.getCC('pEgfr_Lig', 'Vr'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kt', rr.getCC('pEgfr_Lig', 'kt'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kx', rr.getCC('pEgfr_Lig', 'kx'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kf', rr.getCC('pEgfr_Lig', 'kf'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr', rr.getCC('pEgfr_Lig', 'kr'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('ke', rr.getCC('pEgfr_Lig', 'ke'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kh', rr.getCC('pEgfr_Lig', 'kh'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kp1', rr.getCC('pEgfr_Lig', 'kp1'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kp', rr.getCC('pEgfr_Lig', 'kp'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_p', rr.getCC('pEgfr_Lig', 'k_p'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k1', rr.getCC('pEgfr_Lig', 'k1'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_1', rr.getCC('pEgfr_Lig', 'k_1'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k2', rr.getCC('pEgfr_Lig', 'k2'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_2', rr.getCC('pEgfr_Lig', 'k_2'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k3', rr.getCC('pEgfr_Lig', 'k3'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_3', rr.getCC('pEgfr_Lig', 'k_3'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k4', rr.getCC('pEgfr_Lig', 'k4'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_4', rr.getCC('pEgfr_Lig', 'k_4'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k5', rr.getCC('pEgfr_Lig', 'k5'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_5', rr.getCC('pEgfr_Lig', 'k_5'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k6', rr.getCC('pEgfr_Lig', 'k6'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_6', rr.getCC('pEgfr_Lig', 'k_6'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_7', rr.getCC('pEgfr_Lig', 'k_7'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k8', rr.getCC('pEgfr_Lig', 'k8'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_8', rr.getCC('pEgfr_Lig', 'k_8'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k9', rr.getCC('pEgfr_Lig', 'k9'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k10', rr.getCC('pEgfr_Lig', 'k10'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k11', rr.getCC('pEgfr_Lig', 'k11'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_11', rr.getCC('pEgfr_Lig', 'k_11'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k12', rr.getCC('pEgfr_Lig', 'k12'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_12', rr.getCC('pEgfr_Lig', 'k_12'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k13', rr.getCC('pEgfr_Lig', 'k13'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_13' , rr.getCC('pEgfr_Lig', 'k_13'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k14a', rr.getCC('pEgfr_Lig', 'k14a'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k14b', rr.getCC('pEgfr_Lig', 'k14b'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k14c', rr.getCC('pEgfr_Lig', 'k14c'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k15', rr.getCC('pEgfr_Lig', 'k15'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr1a', rr.getCC('pEgfr_Lig', 'kr1a'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr2a', rr.getCC('pEgfr_Lig', 'kr2a'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr1b', rr.getCC('pEgfr_Lig', 'kr1b'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr2b', rr.getCC('pEgfr_Lig', 'kr2b'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr1c', rr.getCC('pEgfr_Lig', 'kr1c'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr2c', rr.getCC('pEgfr_Lig', 'kr2c'))
# quit()


# print('aR_Grb2_pGarem')
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('Vr', rr.getCC('aR_Grb2_pGarem', 'Vr'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kt', rr.getCC('aR_Grb2_pGarem', 'kt'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kx', rr.getCC('aR_Grb2_pGarem', 'kx'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kf', rr.getCC('aR_Grb2_pGarem', 'kf'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr', rr.getCC('aR_Grb2_pGarem', 'kr'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('ke', rr.getCC('aR_Grb2_pGarem', 'ke'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kh', rr.getCC('aR_Grb2_pGarem', 'kh'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kp1', rr.getCC('aR_Grb2_pGarem', 'kp1'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kp', rr.getCC('aR_Grb2_pGarem', 'kp'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_p', rr.getCC('aR_Grb2_pGarem', 'k_p'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k1', rr.getCC('aR_Grb2_pGarem', 'k1'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_1', rr.getCC('aR_Grb2_pGarem', 'k_1'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k2', rr.getCC('aR_Grb2_pGarem', 'k2'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_2', rr.getCC('aR_Grb2_pGarem', 'k_2'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k3', rr.getCC('aR_Grb2_pGarem', 'k3'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_3', rr.getCC('aR_Grb2_pGarem', 'k_3'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k4', rr.getCC('aR_Grb2_pGarem', 'k4'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_4', rr.getCC('aR_Grb2_pGarem', 'k_4'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k5', rr.getCC('aR_Grb2_pGarem', 'k5'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_5', rr.getCC('aR_Grb2_pGarem', 'k_5'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k6', rr.getCC('aR_Grb2_pGarem', 'k6'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_6', rr.getCC('aR_Grb2_pGarem', 'k_6'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_7', rr.getCC('aR_Grb2_pGarem', 'k_7'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k8', rr.getCC('aR_Grb2_pGarem', 'k8'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_8', rr.getCC('aR_Grb2_pGarem', 'k_8'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k9', rr.getCC('aR_Grb2_pGarem', 'k9'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k10', rr.getCC('aR_Grb2_pGarem', 'k10'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k11', rr.getCC('aR_Grb2_pGarem', 'k11'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_11', rr.getCC('aR_Grb2_pGarem', 'k_11'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k12', rr.getCC('aR_Grb2_pGarem', 'k12'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_12', rr.getCC('aR_Grb2_pGarem', 'k_12'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k13', rr.getCC('aR_Grb2_pGarem', 'k13'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_13' , rr.getCC('aR_Grb2_pGarem', 'k_13'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k14a', rr.getCC('aR_Grb2_pGarem', 'k14a'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k14b', rr.getCC('aR_Grb2_pGarem', 'k14b'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k14c', rr.getCC('aR_Grb2_pGarem', 'k14c'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k15', rr.getCC('aR_Grb2_pGarem', 'k15'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr1a', rr.getCC('aR_Grb2_pGarem', 'kr1a'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr2a', rr.getCC('aR_Grb2_pGarem', 'kr2a'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr1b', rr.getCC('aR_Grb2_pGarem', 'kr1b'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr2b', rr.getCC('aR_Grb2_pGarem', 'kr2b'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr1c', rr.getCC('aR_Grb2_pGarem', 'kr1c'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr2c', rr.getCC('aR_Grb2_pGarem', 'kr2c'))
# quit()


# print('aR_Grb2_ppGarem')
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('Vr', rr.getCC('aR_Grb2_ppGarem', 'Vr'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kt', rr.getCC('aR_Grb2_ppGarem', 'kt'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kx', rr.getCC('aR_Grb2_ppGarem', 'kx'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kf', rr.getCC('aR_Grb2_ppGarem', 'kf'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr', rr.getCC('aR_Grb2_ppGarem', 'kr'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('ke', rr.getCC('aR_Grb2_ppGarem', 'ke'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kh', rr.getCC('aR_Grb2_ppGarem', 'kh'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kp1', rr.getCC('aR_Grb2_ppGarem', 'kp1'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kp', rr.getCC('aR_Grb2_ppGarem', 'kp'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_p', rr.getCC('aR_Grb2_ppGarem', 'k_p'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k1', rr.getCC('aR_Grb2_ppGarem', 'k1'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_1', rr.getCC('aR_Grb2_ppGarem', 'k_1'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k2', rr.getCC('aR_Grb2_ppGarem', 'k2'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_2', rr.getCC('aR_Grb2_ppGarem', 'k_2'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k3', rr.getCC('aR_Grb2_ppGarem', 'k3'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_3', rr.getCC('aR_Grb2_ppGarem', 'k_3'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k4', rr.getCC('aR_Grb2_ppGarem', 'k4'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_4', rr.getCC('aR_Grb2_ppGarem', 'k_4'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k5', rr.getCC('aR_Grb2_ppGarem', 'k5'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_5', rr.getCC('aR_Grb2_ppGarem', 'k_5'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k6', rr.getCC('aR_Grb2_ppGarem', 'k6'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_6', rr.getCC('aR_Grb2_ppGarem', 'k_6'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_7', rr.getCC('aR_Grb2_ppGarem', 'k_7'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k8', rr.getCC('aR_Grb2_ppGarem', 'k8'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_8', rr.getCC('aR_Grb2_ppGarem', 'k_8'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k9', rr.getCC('aR_Grb2_ppGarem', 'k9'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k10', rr.getCC('aR_Grb2_ppGarem', 'k10'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k11', rr.getCC('aR_Grb2_ppGarem', 'k11'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_11', rr.getCC('aR_Grb2_ppGarem', 'k_11'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k12', rr.getCC('aR_Grb2_ppGarem', 'k12'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_12', rr.getCC('aR_Grb2_ppGarem', 'k_12'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k13', rr.getCC('aR_Grb2_ppGarem', 'k13'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_13' , rr.getCC('aR_Grb2_ppGarem', 'k_13'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k14a', rr.getCC('aR_Grb2_ppGarem', 'k14a'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k14b', rr.getCC('aR_Grb2_ppGarem', 'k14b'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k14c', rr.getCC('aR_Grb2_ppGarem', 'k14c'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k15', rr.getCC('aR_Grb2_ppGarem', 'k15'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr1a', rr.getCC('aR_Grb2_ppGarem', 'kr1a'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr2a', rr.getCC('aR_Grb2_ppGarem', 'kr2a'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr1b', rr.getCC('aR_Grb2_ppGarem', 'kr1b'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr2b', rr.getCC('aR_Grb2_ppGarem', 'kr2b'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr1c', rr.getCC('aR_Grb2_ppGarem', 'kr1c'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr2c', rr.getCC('aR_Grb2_ppGarem', 'kr2c'))
# quit()


# print('aR_Grb2_ppGarem_pShp2')
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('Vr', rr.getCC('aR_Grb2_ppGarem_pShp2', 'Vr'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kt', rr.getCC('aR_Grb2_ppGarem_pShp2', 'kt'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kx', rr.getCC('aR_Grb2_ppGarem_pShp2', 'kx'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kf', rr.getCC('aR_Grb2_ppGarem_pShp2', 'kf'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr', rr.getCC('aR_Grb2_ppGarem_pShp2', 'kr'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('ke', rr.getCC('aR_Grb2_ppGarem_pShp2', 'ke'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kh', rr.getCC('aR_Grb2_ppGarem_pShp2', 'kh'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kp1', rr.getCC('aR_Grb2_ppGarem_pShp2', 'kp1'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kp', rr.getCC('aR_Grb2_ppGarem_pShp2', 'kp'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_p', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k_p'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k1', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k1'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_1', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k_1'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k2', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k2'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_2', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k_2'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k3', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k3'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_3', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k_3'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k4', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k4'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_4', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k_4'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k5', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k5'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_5', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k_5'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k6', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k6'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_6', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k_6'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_7', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k_7'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k8', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k8'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_8', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k_8'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k9', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k9'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k10', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k10'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k11', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k11'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_11', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k_11'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k12', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k12'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_12', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k_12'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k13', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k13'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_13' , rr.getCC('aR_Grb2_ppGarem_pShp2', 'k_13'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k14a', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k14a'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k14b', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k14b'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k14c', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k14c'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k15', rr.getCC('aR_Grb2_ppGarem_pShp2', 'k15'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr1a', rr.getCC('aR_Grb2_ppGarem_pShp2', 'kr1a'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr2a', rr.getCC('aR_Grb2_ppGarem_pShp2', 'kr2a'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr1b', rr.getCC('aR_Grb2_ppGarem_pShp2', 'kr1b'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr2b', rr.getCC('aR_Grb2_ppGarem_pShp2', 'kr2b'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr1c', rr.getCC('aR_Grb2_ppGarem_pShp2', 'kr1c'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr2c', rr.getCC('aR_Grb2_ppGarem_pShp2', 'kr2c'))
# quit()


# print('aR_Grb2_pGab1')
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('Vr', rr.getCC('aR_Grb2_pGab1', 'Vr'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kt', rr.getCC('aR_Grb2_pGab1', 'kt'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kx', rr.getCC('aR_Grb2_pGab1', 'kx'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kf', rr.getCC('aR_Grb2_pGab1', 'kf'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr', rr.getCC('aR_Grb2_pGab1', 'kr'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('ke', rr.getCC('aR_Grb2_pGab1', 'ke'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kh', rr.getCC('aR_Grb2_pGab1', 'kh'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kp1', rr.getCC('aR_Grb2_pGab1', 'kp1'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kp', rr.getCC('aR_Grb2_pGab1', 'kp'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_p', rr.getCC('aR_Grb2_pGab1', 'k_p'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k1', rr.getCC('aR_Grb2_pGab1', 'k1'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_1', rr.getCC('aR_Grb2_pGab1', 'k_1'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k2', rr.getCC('aR_Grb2_pGab1', 'k2'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_2', rr.getCC('aR_Grb2_pGab1', 'k_2'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k3', rr.getCC('aR_Grb2_pGab1', 'k3'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_3', rr.getCC('aR_Grb2_pGab1', 'k_3'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k4', rr.getCC('aR_Grb2_pGab1', 'k4'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_4', rr.getCC('aR_Grb2_pGab1', 'k_4'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k5', rr.getCC('aR_Grb2_pGab1', 'k5'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_5', rr.getCC('aR_Grb2_pGab1', 'k_5'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k6', rr.getCC('aR_Grb2_pGab1', 'k6'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_6', rr.getCC('aR_Grb2_pGab1', 'k_6'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_7', rr.getCC('aR_Grb2_pGab1', 'k_7'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k8', rr.getCC('aR_Grb2_pGab1', 'k8'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_8', rr.getCC('aR_Grb2_pGab1', 'k_8'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k9', rr.getCC('aR_Grb2_pGab1', 'k9'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k10', rr.getCC('aR_Grb2_pGab1', 'k10'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k11', rr.getCC('aR_Grb2_pGab1', 'k11'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_11', rr.getCC('aR_Grb2_pGab1', 'k_11'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k12', rr.getCC('aR_Grb2_pGab1', 'k12'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_12', rr.getCC('aR_Grb2_pGab1', 'k_12'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k13', rr.getCC('aR_Grb2_pGab1', 'k13'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_13' , rr.getCC('aR_Grb2_pGab1', 'k_13'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k14a', rr.getCC('aR_Grb2_pGab1', 'k14a'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k14b', rr.getCC('aR_Grb2_pGab1', 'k14b'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k14c', rr.getCC('aR_Grb2_pGab1', 'k14c'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k15', rr.getCC('aR_Grb2_pGab1', 'k15'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr1a', rr.getCC('aR_Grb2_pGab1', 'kr1a'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr2a', rr.getCC('aR_Grb2_pGab1', 'kr2a'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr1b', rr.getCC('aR_Grb2_pGab1', 'kr1b'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr2b', rr.getCC('aR_Grb2_pGab1', 'kr2b'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr1c', rr.getCC('aR_Grb2_pGab1', 'kr1c'))
#
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr2c', rr.getCC('aR_Grb2_pGab1', 'kr2c'))
# quit()


# print('aR_Grb2_ppGab1')
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('Vr', rr.getCC('aR_Grb2_ppGab1', 'Vr'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kt', rr.getCC('aR_Grb2_ppGab1', 'kt'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kx', rr.getCC('aR_Grb2_ppGab1', 'kx'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kf', rr.getCC('aR_Grb2_ppGab1', 'kf'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr', rr.getCC('aR_Grb2_ppGab1', 'kr'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('ke', rr.getCC('aR_Grb2_ppGab1', 'ke'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kh', rr.getCC('aR_Grb2_ppGab1', 'kh'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kp1', rr.getCC('aR_Grb2_ppGab1', 'kp1'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kp', rr.getCC('aR_Grb2_ppGab1', 'kp'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_p', rr.getCC('aR_Grb2_ppGab1', 'k_p'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k1', rr.getCC('aR_Grb2_ppGab1', 'k1'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_1', rr.getCC('aR_Grb2_ppGab1', 'k_1'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k2', rr.getCC('aR_Grb2_ppGab1', 'k2'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_2', rr.getCC('aR_Grb2_ppGab1', 'k_2'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k3', rr.getCC('aR_Grb2_ppGab1', 'k3'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_3', rr.getCC('aR_Grb2_ppGab1', 'k_3'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k4', rr.getCC('aR_Grb2_ppGab1', 'k4'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_4', rr.getCC('aR_Grb2_ppGab1', 'k_4'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k5', rr.getCC('aR_Grb2_ppGab1', 'k5'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_5', rr.getCC('aR_Grb2_ppGab1', 'k_5'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k6', rr.getCC('aR_Grb2_ppGab1', 'k6'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_6', rr.getCC('aR_Grb2_ppGab1', 'k_6'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_7', rr.getCC('aR_Grb2_ppGab1', 'k_7'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k8', rr.getCC('aR_Grb2_ppGab1', 'k8'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_8', rr.getCC('aR_Grb2_ppGab1', 'k_8'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k9', rr.getCC('aR_Grb2_ppGab1', 'k9'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k10', rr.getCC('aR_Grb2_ppGab1', 'k10'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k11', rr.getCC('aR_Grb2_ppGab1', 'k11'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_11', rr.getCC('aR_Grb2_ppGab1', 'k_11'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k12', rr.getCC('aR_Grb2_ppGab1', 'k12'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_12', rr.getCC('aR_Grb2_ppGab1', 'k_12'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k13', rr.getCC('aR_Grb2_ppGab1', 'k13'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_13' , rr.getCC('aR_Grb2_ppGab1', 'k_13'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k14a', rr.getCC('aR_Grb2_ppGab1', 'k14a'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k14b', rr.getCC('aR_Grb2_ppGab1', 'k14b'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k14c', rr.getCC('aR_Grb2_ppGab1', 'k14c'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k15', rr.getCC('aR_Grb2_ppGab1', 'k15'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr1a', rr.getCC('aR_Grb2_ppGab1', 'kr1a'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr2a', rr.getCC('aR_Grb2_ppGab1', 'kr2a'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr1b', rr.getCC('aR_Grb2_ppGab1', 'kr1b'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr2b', rr.getCC('aR_Grb2_ppGab1', 'kr2b'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr1c', rr.getCC('aR_Grb2_ppGab1', 'kr1c'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr2c', rr.getCC('aR_Grb2_ppGab1', 'kr2c'))
# quit()

# 
# print('aR_Grb2_ppGab1_pShp2')
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('Vr', rr.getCC('aR_Grb2_ppGab1_pShp2', 'Vr'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kt', rr.getCC('aR_Grb2_ppGab1_pShp2', 'kt'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kx', rr.getCC('aR_Grb2_ppGab1_pShp2', 'kx'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kf', rr.getCC('aR_Grb2_ppGab1_pShp2', 'kf'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr', rr.getCC('aR_Grb2_ppGab1_pShp2', 'kr'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('ke', rr.getCC('aR_Grb2_ppGab1_pShp2', 'ke'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kh', rr.getCC('aR_Grb2_ppGab1_pShp2', 'kh'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kp1', rr.getCC('aR_Grb2_ppGab1_pShp2', 'kp1'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kp', rr.getCC('aR_Grb2_ppGab1_pShp2', 'kp'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_p', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k_p'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k1', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k1'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_1', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k_1'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k2', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k2'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_2', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k_2'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k3', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k3'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_3', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k_3'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k4', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k4'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_4', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k_4'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k5', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k5'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_5', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k_5'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k6', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k6'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_6', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k_6'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_7', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k_7'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k8', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k8'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_8', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k_8'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k9', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k9'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k10', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k10'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k11', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k11'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_11', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k_11'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k12', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k12'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_12', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k_12'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k13', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k13'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k_13' , rr.getCC('aR_Grb2_ppGab1_pShp2', 'k_13'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k14a', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k14a'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k14b', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k14b'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k14c', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k14c'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('k15', rr.getCC('aR_Grb2_ppGab1_pShp2', 'k15'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr1a', rr.getCC('aR_Grb2_ppGab1_pShp2', 'kr1a'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr2a', rr.getCC('aR_Grb2_ppGab1_pShp2', 'kr2a'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr1b', rr.getCC('aR_Grb2_ppGab1_pShp2', 'kr1b'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr2b', rr.getCC('aR_Grb2_ppGab1_pShp2', 'kr2b'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr1c', rr.getCC('aR_Grb2_ppGab1_pShp2', 'kr1c'))
# 
# rr.reset()
# # rr.simulate(0, 700, 701)
# print('kr2c', rr.getCC('aR_Grb2_ppGab1_pShp2', 'kr2c'))
# quit()


# print('aR_pShc1')
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('Vr', rr.getCC('aR_pShc1', 'Vr'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kt', rr.getCC('aR_pShc1', 'kt'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kx', rr.getCC('aR_pShc1', 'kx'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kf', rr.getCC('aR_pShc1', 'kf'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr', rr.getCC('aR_pShc1', 'kr'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('ke', rr.getCC('aR_pShc1', 'ke'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kh', rr.getCC('aR_pShc1', 'kh'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kp1', rr.getCC('aR_pShc1', 'kp1'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kp', rr.getCC('aR_pShc1', 'kp'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_p', rr.getCC('aR_pShc1', 'k_p'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k1', rr.getCC('aR_pShc1', 'k1'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_1', rr.getCC('aR_pShc1', 'k_1'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k2', rr.getCC('aR_pShc1', 'k2'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_2', rr.getCC('aR_pShc1', 'k_2'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k3', rr.getCC('aR_pShc1', 'k3'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_3', rr.getCC('aR_pShc1', 'k_3'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k4', rr.getCC('aR_pShc1', 'k4'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_4', rr.getCC('aR_pShc1', 'k_4'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k5', rr.getCC('aR_pShc1', 'k5'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_5', rr.getCC('aR_pShc1', 'k_5'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k6', rr.getCC('aR_pShc1', 'k6'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_6', rr.getCC('aR_pShc1', 'k_6'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_7', rr.getCC('aR_pShc1', 'k_7'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k8', rr.getCC('aR_pShc1', 'k8'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_8', rr.getCC('aR_pShc1', 'k_8'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k9', rr.getCC('aR_pShc1', 'k9'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k10', rr.getCC('aR_pShc1', 'k10'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k11', rr.getCC('aR_pShc1', 'k11'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_11', rr.getCC('aR_pShc1', 'k_11'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k12', rr.getCC('aR_pShc1', 'k12'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_12', rr.getCC('aR_pShc1', 'k_12'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k13', rr.getCC('aR_pShc1', 'k13'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k_13' , rr.getCC('aR_pShc1', 'k_13'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k14a', rr.getCC('aR_pShc1', 'k14a'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k14b', rr.getCC('aR_pShc1', 'k14b'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k14c', rr.getCC('aR_pShc1', 'k14c'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('k15', rr.getCC('aR_pShc1', 'k15'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr1a', rr.getCC('aR_pShc1', 'kr1a'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr2a', rr.getCC('aR_pShc1', 'kr2a'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr1b', rr.getCC('aR_pShc1', 'kr1b'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr2b', rr.getCC('aR_pShc1', 'kr2b'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr1c', rr.getCC('aR_pShc1', 'kr1c'))
# 
# rr.reset()
# rr.simulate(0, 700, 701)
# print('kr2c', rr.getCC('aR_pShc1', 'kr2c'))
# quit()


print('pSOS1')

rr.reset()
# rr.simulate(0, 700, 701)
print('Vr', rr.getCC('pSOS1', 'Vr'))

rr.reset()
# rr.simulate(0, 700, 701)
print('kt', rr.getCC('pSOS1', 'kt'))

rr.reset()
# rr.simulate(0, 700, 701)
print('kx', rr.getCC('pSOS1', 'kx'))

rr.reset()
# rr.simulate(0, 700, 701)
print('kf', rr.getCC('pSOS1', 'kf'))

rr.reset()
# rr.simulate(0, 700, 701)
print('kr', rr.getCC('pSOS1', 'kr'))

rr.reset()
# rr.simulate(0, 700, 701)
print('ke', rr.getCC('pSOS1', 'ke'))

rr.reset()
# rr.simulate(0, 700, 701)
print('kh', rr.getCC('pSOS1', 'kh'))

rr.reset()
# rr.simulate(0, 700, 701)
print('kp1', rr.getCC('pSOS1', 'kp1'))

rr.reset()
# rr.simulate(0, 700, 701)
print('kp', rr.getCC('pSOS1', 'kp'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k_p', rr.getCC('pSOS1', 'k_p'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k1', rr.getCC('pSOS1', 'k1'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k_1', rr.getCC('pSOS1', 'k_1'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k2', rr.getCC('pSOS1', 'k2'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k_2', rr.getCC('pSOS1', 'k_2'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k3', rr.getCC('pSOS1', 'k3'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k_3', rr.getCC('pSOS1', 'k_3'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k4', rr.getCC('pSOS1', 'k4'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k_4', rr.getCC('pSOS1', 'k_4'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k5', rr.getCC('pSOS1', 'k5'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k_5', rr.getCC('pSOS1', 'k_5'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k6', rr.getCC('pSOS1', 'k6'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k_6', rr.getCC('pSOS1', 'k_6'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k_7', rr.getCC('pSOS1', 'k_7'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k8', rr.getCC('pSOS1', 'k8'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k_8', rr.getCC('pSOS1', 'k_8'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k9', rr.getCC('pSOS1', 'k9'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k10', rr.getCC('pSOS1', 'k10'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k11', rr.getCC('pSOS1', 'k11'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k_11', rr.getCC('pSOS1', 'k_11'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k12', rr.getCC('pSOS1', 'k12'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k_12', rr.getCC('pSOS1', 'k_12'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k13', rr.getCC('pSOS1', 'k13'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k_13' , rr.getCC('pSOS1', 'k_13'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k14a', rr.getCC('pSOS1', 'k14a'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k14b', rr.getCC('pSOS1', 'k14b'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k14c', rr.getCC('pSOS1', 'k14c'))

rr.reset()
# rr.simulate(0, 700, 701)
print('k15', rr.getCC('pSOS1', 'k15'))

rr.reset()
# rr.simulate(0, 700, 701)
print('kr1a', rr.getCC('pSOS1', 'kr1a'))

rr.reset()
# rr.simulate(0, 700, 701)
print('kr2a', rr.getCC('pSOS1', 'kr2a'))

rr.reset()
# rr.simulate(0, 700, 701)
print('kr1b', rr.getCC('pSOS1', 'kr1b'))

rr.reset()
# rr.simulate(0, 700, 701)
print('kr2b', rr.getCC('pSOS1', 'kr2b'))

rr.reset()
# rr.simulate(0, 700, 701)
print('kr1c', rr.getCC('pSOS1', 'kr1c'))

rr.reset()
# rr.simulate(0, 700, 701)
print('kr2c', rr.getCC('pSOS1', 'kr2c'))
quit()
