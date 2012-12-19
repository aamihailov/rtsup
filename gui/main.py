from connection import Connection

def main():
    c = Connection('amihailov.pro', '/rtsup/api')
    succeed, employees = c.get_employee_list()
    print employees
    if succeed:
        print employees['objects'][0]['addr']

if __name__ == '__main__':
    main()