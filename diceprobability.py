import math
# Probability is two dice where thrown
# A = math.floor(A)
# B = math.ceil(B)

int_samplespace = [
                11,22,33,44,55,66,12,13,14,15,16,21,23,24,25,26,31,32,
                34,35,36,41,42,43,45,46,51,52,53,54,56,61,62,63,64,65
               ]
obj_samplespace = [
                '11','22','33','44','55','66','12','13','14','15','16','21','23','24','25','26','31','32',
                '34','35','36','41','42','43','45','46','51','52','53','54','56','61','62','63','64','65'
                ]
print(int_samplespace)
# print(len(int_samplespace))
# print(obj_samplespace)
# print(len(obj_samplespace))

def obj_probability(outcome):
    result = len(outcome)/len(obj_samplespace)
    return result

def int_probability(outcome):
    result = len(outcome)/len(int_samplespace)
    return result

# (A) chances of getting two faces with equal numbers AKA a double
A_outcome = [11,22,33,44,55,66]
A = int_probability(A_outcome)
# (A) = 0.166 i.e 16.6%

# (B) chances of getting only one out off all the outcome in the samplespace
B_outcome = [11]
B = int_probability(B_outcome)
# (B) = 0.027 i.e 0.027%

# (C) chances of getting a sum of 3
C_outcome = [12,21]
C = int_probability(C_outcome)
# (C) = 0.05 i.e 0.05%

# (D) chances of getting a sum of 4
D_outcome = [13,31,22]
D = int_probability(D_outcome)
# (D) = 0.08 i.e 0.08%

# (E) chances of getting a sum of 5
E_outcome = [23,32,14,41]
E = int_probability(E_outcome)
# (E) = 0.111 i.e 11.1%

# (F) chances of getting a sum of 6
F_outcome = [33,15,51,42,24]
F = int_probability(F_outcome)
# (F) = 0.138 i.e 13.8%

# (G) chances of getting a sum of 7
G_outcome = [16,61,25,52,34,43]
G = int_probability(G_outcome)
# (G) = 0.166 i.e 16.6%

# (H) chances of getting a sum of 8
H_outcome = [26,62,35,53,44]
H = int_probability(H_outcome)
# (H) = 0.138 i.e 13.8%

# (I) chances of getting a sum of 9
I_outcome = [36,63,45,54]
I = int_probability(I_outcome)
# (I) = 0.111 i.e 11.1%

# (J) chances of getting a sum of 10
J_outcome = [55,46,64]
J = int_probability(J_outcome)
# (J) = 0.08 i.e 0.08%

# (K) chances of getting a sum of 11
K_outcome = [56,65]
K = int_probability(K_outcome)
# (K) = 0.05 i.e 0.05%