import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

class Body:
    def __init__(self, mass, x, y, vx, vy):
        self.mass = mass
        self.pos = np.array([x, y])
        self.vel = np.array([vx, vy])

class State:
    def __init__(self):
        self.time = 0.0
        selection = 0

        print("Select initial conditions")
        print("1. Skew")
        print("2. Random")
        print("3. Manual")

        while selection not in {"1", "2", "3"}:
            selection = input()

        if selection == "1":
            self.body1 = Body(1.0, 0.3, 0.5, 0.0, 0.0)
            self.body2 = Body(1.0, 0.2, -0.1, 0.0, 0.0)
            self.body3 = Body(1.0, -0.5, -0.4, 0.0, 0.0)
            
        elif selection == "2":
            self.body1 = Body(random.uniform(0.0,5.0), 
                              random.uniform(-3.0,3.0), 
                              random.uniform(-3.0,3.0), 
                              random.uniform(-1.0,1.0), 
                              random.uniform(-1.0,1.0))
            self.body2 = Body(random.uniform(0.0,5.0), 
                              random.uniform(-3.0,3.0), 
                              random.uniform(-3.0,3.0), 
                              random.uniform(-1.0,1.0), 
                              random.uniform(-1.0,1.0))
            self.body3 = Body(random.uniform(0.0,5.0), 
                              random.uniform(-3.0,3.0), 
                              random.uniform(-3.0,3.0), 
                              random.uniform(-1.0,1.0), 
                              random.uniform(-1.0,1.0))

        elif selection == "3":
            print("Body 1:")
            self.body1 = Body(float(input("m = ")),
                              float(input("x(0) = ")),
                              float(input("y(0) = ")),
                              float(input("v_x(0) = ")),
                              float(input("v_y(0) = ")))
            print("Body 2:")
            self.body2 = Body(float(input("m = ")),
                              float(input("x(0) = ")),
                              float(input("y(0) = ")),
                              float(input("v_x(0) = ")),
                              float(input("v_y(0) = ")))
            print("Body 3:")
            self.body3 = Body(float(input("m = ")),
                              float(input("x(0) = ")),
                              float(input("y(0) = ")),
                              float(input("v_x(0) = ")),
                              float(input("v_y(0) = ")))

    def printState(self):
        print("t = "+format(self.time,'.3f'))
        print("Body 1: m = "+format(self.body1.mass,'.3f')+"; (x(t), y(t)) = ("+format(self.body1.pos[0],'.3f')+", "+format(self.body1.pos[1],'.3f')+"); (v_x(t), v_y(t)) = ("+format(self.body1.vel[0],'.3f')+", "+format(self.body1.vel[1],'.3f')+")")
        print("Body 2: m = "+format(self.body2.mass,'.3f')+"; (x(t), y(t)) = ("+format(self.body2.pos[0],'.3f')+", "+format(self.body2.pos[1],'.3f')+"); (v_x(t), v_y(t)) = ("+format(self.body2.vel[0],'.3f')+", "+format(self.body2.vel[1],'.3f')+")")
        print("Body 3: m = "+format(self.body3.mass,'.3f')+"; (x(t), y(t)) = ("+format(self.body3.pos[0],'.3f')+", "+format(self.body3.pos[1],'.3f')+"); (v_x(t), v_y(t)) = ("+format(self.body3.vel[0],'.3f')+", "+format(self.body3.vel[1],'.3f')+")\n")
        return
    
def f(x):
    G = 1
    y = np.zeros(12)
    m1 = state.body1.mass
    m2 = state.body2.mass
    m3 = state.body3.mass
    p1 = np.array([x[0], x[2]])
    p2 = np.array([x[4], x[6]])
    p3 = np.array([x[8], x[10]])
    d12 = np.linalg.norm(p1-p2)
    if d12 < 0.15:
        d12 = 0.15
    # elif d12 > 0.3:
    #     d12 = 0.3
    d13 = np.linalg.norm(p1-p3)
    if d13 < 0.15:
        d13 = 0.15
    # elif d13 > 0.3:
    #     d13 = 0.3    
    d23 = np.linalg.norm(p2-p3)
    if d23 < 0.15:
        d23 = 0.15
    # elif d23 > 0.3:
    #     d23 = 0.3
    for i in range(0,12,2):
        y[i] = x[i+1]
    y[1] = -1 * G * ((m2 * ((p1[0] - p2[0]) / np.power(d12,3))) + (m3 * ((p1[0] - p3[0]) / np.power(d13,3))))
    y[3] = -1 * G * ((m2 * ((p1[1] - p2[1]) / np.power(d12,3))) + (m3 * ((p1[1] - p3[1]) / np.power(d13,3))))
    y[5] = -1 * G * ((m1 * ((p2[0] - p1[0]) / np.power(d12,3))) + (m3 * ((p2[0] - p3[0]) / np.power(d23,3))))
    y[7] = -1 * G * ((m1 * ((p2[1] - p1[1]) / np.power(d12,3))) + (m3 * ((p2[1] - p3[1]) / np.power(d23,3))))
    y[9] = -1 * G * ((m1 * ((p3[0] - p1[0]) / np.power(d13,3))) + (m2 * ((p3[0] - p2[0]) / np.power(d23,3))))
    y[11] = -1 * G * ((m1 * ((p3[1] - p1[1]) / np.power(d13,3))) + (m2 * ((p3[1] - p2[1]) / np.power(d23,3))))
    return y

def rungeKutta(x0):
    h = timeStep
    k1 = f(x0)
    k2 = f(x0 + ((h * k1) / 2))
    k3 = f(x0 + ((h * k2) / 2))
    k4 = f(x0 + (h * k3))
    x1 = x0 + (((k1 + (2 * k2) + (2 * k3) + k4) * h) / 6)
    return x1

def updateState():
    state.time += timeStep
    x1 = state.body1.pos[0]
    y1 = state.body1.pos[1]
    x2 = state.body2.pos[0]
    y2 = state.body2.pos[1]
    x3 = state.body3.pos[0]
    y3 = state.body3.pos[1]
    vx1 = state.body1.vel[0]
    vy1 = state.body1.vel[1]
    vx2 = state.body2.vel[0]
    vy2 = state.body2.vel[1]
    vx3 = state.body3.vel[0]
    vy3 = state.body3.vel[1]
    x = [x1, vx1, y1, vy1, x2, vx2, y2, vy2, x3, vx3, y3, vy3]
    y = rungeKutta(x)
    state.body1.pos[0] = y[0]
    state.body1.vel[0] = y[1]
    state.body1.pos[1] = y[2]
    state.body1.vel[1] = y[3]
    state.body2.pos[0] = y[4]
    state.body2.vel[0] = y[5]
    state.body2.pos[1] = y[6]
    state.body2.vel[1] = y[7]
    state.body3.pos[0] = y[8]
    state.body3.vel[0] = y[9]
    state.body3.pos[1] = y[10]
    state.body3.vel[1] = y[11]
    return

def generatePath():
    x = np.array([0,state.body1.pos[0],state.body2.pos[0],state.body3.pos[0]])
    y = np.array([0,state.body1.pos[1],state.body2.pos[1],state.body3.pos[1]])
    colors = np.array([[0,0,0,1],[1,0,0,1],[0,1,0,1],[0,0,1,1]])
    fig, ax = plt.subplots()
    points = ax.scatter(x, y, c=colors)
    plt.axis('off')

    def animate(frame):
        state.printState()
        updateState()
        x = np.array([0,state.body1.pos[0],state.body2.pos[0],state.body3.pos[0]])
        y = np.array([0,state.body1.pos[1],state.body2.pos[1],state.body3.pos[1]])
        points.set_offsets(np.transpose([x, y]))
        return [points]

    ani = anim.FuncAnimation(fig, animate, frames=100, interval=1, blit=True)

    plt.xlim(-3,3)
    plt.ylim(-3,3)
    plt.show()
    return

timeStep = 0.005
state = State()
generatePath()