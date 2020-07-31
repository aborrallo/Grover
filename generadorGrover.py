
if __name__ == '__main__':


    import qiskit
    import numpy as np
    from qiskit import QuantumProgram 
    import math
    from qiskit.tools.visualization import plot_histogram
    from qiskit import Gate
    from qiskit import CompositeGate
    from scipy.optimize import newton

# Creating Programs create your first QuantumProgram object instance.
    qp = QuantumProgram()

# Set your API Token
# You can get it from https://quantumexperience.ng.bluemix.net/qx/account,
# looking for "Personal Access Token" section.
    QX_TOKEN = '58630be1e0bfd1b1dbdc6ef326a98c1c983883e8b8c64a5d0d37f2ebe0684e6e595d6850fd2f761d6a76bdd3dba7d6efe89f1166d85a8c7835842458d86ac01a'
    QX_URL = "https://quantumexperience.ng.bluemix.net/api"

# Set up the API and execute the program.
# You need the API Token and the QX URL.
    qp.set_api(QX_TOKEN, QX_URL)

#This function return a list with the number of qubits in the first position and 
# another list in the second element that contain the desired element but in string type    

    
    
    def __asker__():
        item=[]
        nQubitsItem=[]
        item_binario = str(input("Introduce the desired item on binary (it should be an item with a number of qubits between two and five (both are includes)): "))
        item=list(item_binario)
        nQubitsItem=[len(str(item_binario)),item]
        while(nQubitsItem[0]<2 or nQubitsItem[0]>5):
                    item_binario = str(input("Introduce the desired item please (IT SOULD BE AN ITEM WITH A NUMBER OF QUBITS BETWEEN TWO AND FIVE (both are includes)): "))
                    item=list(item_binario)
                    nQubitsItem=[len(str(item_binario)),item]
        print("this is a quantum simulation, be patient.....")
        return(nQubitsItem)
 

#This is an auxiliary function, the root of this function give us the number of aplications
# of the kernel        
    
    def __AuxiliaryFunction__(x,d):
        
        
        return (2*x+1)*math.asin(1/math.sqrt(d))-math.pi/2

#this is the function that compute the number of aplications of the kernel by obtaining
# the root of the equation before        
    
    def __Solver__(d):
        
      
        
        def Function(x):
            return (2*x+1)*math.asin(1/math.sqrt(d))-math.pi/2
        
        solution=newton(Function,1)
        IntegerPart=int(solution)
        
        if solution-IntegerPart < 0.8:
            solution=IntegerPart
        else:
            solution=IntegerPart+1
            
        return solution

#This function build grover's circuit 
        
    def GeneradorGroverCircuit():
        
        nQubitsItem=__asker__()
        d=pow(2,nQubitsItem[0])
        Naplications=__Solver__(d)

                        
        qr = qp.create_quantum_register('qr',nQubitsItem[0])
        cr = qp.create_classical_register('cr',nQubitsItem[0])
        qc = qp.create_circuit('GROVER',[qr],[cr])
        
        
###################################################################################      
        
        def CCCNOT():
            qc.ccx(qr[0],qr[1],qr[2]) 
            qc.ccx(qr[1],qr[2],qr[3])
            qc.ccx(qr[0],qr[1],qr[2]) 
            qc.ccx(qr[1],qr[2],qr[3])

        def CCCsqrtZ():
            x=0.39269908169872415480783042290993786052464617492188822762186572449001
            xt=-0.39269908169872415480783042290993786052464617492188822762186572449001
            qc.cu1(x,qr[0],qr[4])
            qc.cx(qr[0],qr[1])
            qc.cu1(xt,qr[1],qr[4])
            qc.cx(qr[0],qr[1])
            qc.cu1(x,qr[1],qr[4])
            qc.cx(qr[1],qr[2])
            qc.cu1(xt,qr[2],qr[4])
            qc.cx(qr[0],qr[2])
            qc.cu1(x,qr[2],qr[4])
            qc.cx(qr[1],qr[2])
            qc.cu1(xt,qr[2],qr[4])
            qc.cx(qr[0],qr[2])
            qc.cu1(x,qr[2],qr[4]) 

        def fiveQubits():
            qc.cu1(math.pi/2,qr[3],qr[4])
            CCCNOT()
            qc.cu1(3*math.pi/2,qr[3],qr[4])
            CCCNOT()
            CCCsqrtZ()
        
        def threeQubits():
            qc.cu1(math.pi/2,qr[1],qr[2])
            qc.cx(qr[0],qr[1])
            qc.cu1(3*math.pi/2,qr[1],qr[2])
            qc.cx(qr[0],qr[1])
            qc.cu1(math.pi/2,qr[0],qr[2])
        

        def fourQubits():
            x= 0.7853981633974483096156608458198757210492923498437764552437361480
            xt=-0.7853981633974483096156608458198757210492923498437764552437361480
            qc.cu1(x,qr[0],qr[3])
            qc.cx(qr[0],qr[1])
            qc.cu1(xt,qr[1],qr[3])
            qc.cx(qr[0],qr[1])
            qc.cu1(x,qr[1],qr[3])
            qc.cx(qr[1],qr[2])
            qc.cu1(xt,qr[2],qr[3])
            qc.cx(qr[0],qr[2])
            qc.cu1(x,qr[2],qr[3])
            qc.cx(qr[1],qr[2])
            qc.cu1(xt,qr[2],qr[3])
            qc.cx(qr[0],qr[2])
            qc.cu1(x,qr[2],qr[3])
            
        def twoQubits():
            qc.cz(qr[0],qr[1])

###################################################################################
        
        for i in range(nQubitsItem[0]):
            qc.h(qr[i])
        
        for i in range(Naplications):
            
            for i in range(nQubitsItem[0]):
                bit=int(nQubitsItem[1][i])
                if bit==0:
                    qc.x(qr[i])
            
            if nQubitsItem[0]==2:
                twoQubits()
            elif nQubitsItem[0]==3:
                threeQubits()
            elif nQubitsItem[0]==4:
                fourQubits()
            elif nQubitsItem[0]==5:
                fiveQubits()
               
            
            for i in range(nQubitsItem[0]):
                bit=int(nQubitsItem[1][i])
                if bit==0:
                    qc.x(qr[i])
           
            for i in range(nQubitsItem[0]):
                qc.h(qr[i])
         
            for i in range(nQubitsItem[0]):
                qc.x(qr[i])    
            
            
            if nQubitsItem[0]==2:
                twoQubits()
            elif nQubitsItem[0]==3:
                threeQubits()
            elif nQubitsItem[0]==4:
                fourQubits()
            elif nQubitsItem[0]==5:
                fiveQubits()
        
            for i in range(nQubitsItem[0]):
                qc.x(qr[i])
            
            for i in range(nQubitsItem[0]):
                qc.h(qr[i])
                
        for i in range(nQubitsItem[0]):
                qc.measure(qr[i],cr[i])     

    
                
    GeneradorGroverCircuit() 

    

    result = qp.execute(["GROVER"])
    plot_histogram(result.get_counts('GROVER')) 
    print("Remember than in Qiskit's histograms the binary numbers should be read starting by the end")
        