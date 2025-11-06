import re

def searchFirstLetter(string): #первая буква в строке
    regular = r'[A-Za-zА-Яа-я()]'

def findAllRoles(lines): #роли в файле
        roles = {}
        lastLine = 0
        
        for i, line in enumerate(lines):
            if 'textLines' in line:
                break
            role_name = line.strip()
            if role_name:
                roles[role_name] = ''
            lastLine = i + 1
        return roles, lastLine

def numerateReplicasAndAddReplicasToRoles(lines, lastLine, roles):
        replicas = {}
        cnt = 0
        
        for x in range(lastLine + 1, len(lines)):
            current_line = lines[x].strip()
            if not current_line:
                continue  #пустые строки
                
            if not lines[x].startswith(' '):
                cnt += 1
                if ':' in lines[x]:
                    role, replica_text = lines[x].split(':', 1)
                    role = role.strip()
                    replicas[cnt] = replica_text.strip()
                    if role in roles:
                        roles[role] += f'{cnt};'
                else:
                    replicas[cnt] = lines[x].strip()
            else:
                replicas[cnt] += ' ' + lines[x].strip()
        return replicas

def writeToFile(file, roles, replicas): #zapis v fail
        for role, replica_numbers in roles.items():
            if not replica_numbers:
                continue
                
            file.write(f'{role}:\n')
            numbers_of_replicas = replica_numbers.split(';')[:-1]
            
            for number in numbers_of_replicas:
                if number.isdigit():
                    replica_id = int(number)
                    if replica_id in replicas:
                        replica_text = replicas[replica_id]
                        file.write(f'{number}) {replica_text}\n')
            
            file.write('\n')
        
        print("Сценарий готов и записан в файл out.txt")
   
def main():
        with open('/7. Дз работа с файлами/roles.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()[1:]
        
        with open('/7. Дз работа с файлами/out.txt', 'w', encoding='utf-8') as outFile:
            roles, lastLine = findAllRoles(lines)
            replicas = numerateReplicasAndAddReplicasToRoles(lines, lastLine, roles)
            writeToFile(outFile, roles, replicas)
   
if __name__ == "__main__":
    main()