import matplotlib.pyplot as plt
import numpy as np
import control

# Define the transfer function G(s)
s = control.TransferFunction([12], [4, 10, 5])

# Transfer function G(s)
print("Transfer function:")
print(s)

# Feedback of G(s) with K=1
G_fb = control.feedback(s, 1)
print("Feedback function:")
print(G_fb)

# Step response
t, y = control.step_response(G_fb)
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response')
plt.grid(True)
plt.show()

# Bode plot
control.bode_plot(s)
plt.grid(True)
plt.show()

# Nyquist plot
omega = np.logspace(-2, 2, num=1000)  # Frequency range
control.nyquist_plot(s, omega)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Nyquist Plot')
plt.grid(True)
plt.show()

# Root locus plot
rlist, klist = control.root_locus(s)
plt.plot(np.real(rlist), np.imag(rlist), 'b')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Root Locus Plot')
plt.grid(True)
plt.show()

# Pole-zero map
control.pzmap(s)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Pole-Zero Map')
plt.grid(True)
plt.show()

# Damping factor and poles
damping_info = control.damp(s)
print("Damping Factor:")
print(damping_info[0])
print("Poles:")
print(damping_info[1])

# Zeros
zeros = control.zeros(s)
print("Zeros:")
print(zeros)
