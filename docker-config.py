def main():
    welcome()
    OS_version  = get_values()
    write_docker(OS_version)




def welcome():
    print('Welcome to the Docker configuration script.')
    print('Answer each questions from the given options or choose NULL \nto get the Dockerfile according to your requirements.')


def get_values():

    cpu_gpu=""
    OS_version=""
    cpu_os = ['ubuntu', 'ubuntu:20.04', 'ubuntu:18.04']
    gpu_os = ['nvidia/cuda', 'nvidia/cuda:11.2.1-devel-ubuntu20.04', 'nvidia/cuda:10.2-devel-ubuntu18.04']
    
    # To check if program needs a CPU or GPU
    while(cpu_gpu.lower() not in ['yes', 'no']):
        cpu_gpu=input("Do you need a GPU support? Enter (yes/no): ")
    
    # To provide the options according to the CPU or GPU requirements.
    print('Enter the base operating system for your requirement.')
    print('The available options are:', end=" ")
    if(cpu_gpu.lower == 'n'):
        print(*cpu_os, sep=', ')
        OS_version=input()
    else:
        print(*gpu_os, sep=', ')
        OS_version=input()

    return OS_version




def write_docker(OS_version):
    print(f'''
    FROM {OS_version}
    
    ''')
    








    OS_version=""
    
    
    print()
    OS_version = input()




if __name__=='__main__':
    main()