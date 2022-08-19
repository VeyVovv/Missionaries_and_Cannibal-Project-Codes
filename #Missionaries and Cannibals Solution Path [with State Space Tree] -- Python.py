
from queue import deque

class State:
  def __init__(self, mssnry, cnbl , shore):
    self.mssnry = mssnry
    self.cnbl = cnbl
    self.shore = shore
    
  __invalidList = [[1,2,1],[1,3,1],[2,3,1],[2,1,0],[2,0,0],[2,1,1],[1,0,0],[1,3,0],[1,2,0],[1,3,0],[2,3,0]]     #If cannibal is greater than missionary when at least one missionary is present and
     # For cases like 2 missionaries but cannibal is 1 here so that means 2 cannibal and 1 missionary in other side
  
  def __repr__(self):
    return "[ State (%s, %s, %s) ]" % ( self.mssnry, self.cnbl, self.shore)    
   
    
  def algorithm(self):
    for a in range(3):
      m = a;
      for b in range(3):
        c = b;
        if self.shore == 1 :  
          children = State(self.mssnry-m, self.cnbl-c, self.shore-1);
        else:
          children = State(self.mssnry+m, self.cnbl+c, self.shore+1);   
        if m+c >= 1 and m+c <= 2 and children.condition():    
            action = "%s" % ( children)
            
            yield action, children
            
  def val(self):
      return ([self.mssnry, self.cnbl, self.shore])
            
  def condition(self):
    if self.mssnry < 0 or self.cnbl < 0 or self.mssnry > 3 or self.cnbl > 3 or (self.shore != 0 and self.shore != 1):
        return False
  
    if self.val() in self.__invalidList:
        return False

    else:
        return True

  def is_finalstate(self):
    return self.cnbl == 0 and self.mssnry == 0 and self.shore == 0

  


class Node:  
  def __init__(self, parent_node, state, action, depth):
    self.parent_node = parent_node
    self.state = state
    self.action = action
    self.depth = depth
  
  def recursion(self):
    for (action, succ_state) in self.state.algorithm():
      children_node = Node(
                       parent_node=self,
                       state=succ_state,
                       action=action,
                       depth=self.depth + 1)
      yield children_node
  
  def extract_solution(self):
    solution = []
    node = self
    while node.parent_node is not None:
      solution.append(node.action)
      node = node.parent_node
    solution.reverse()
    return solution


def bfs_search(insertnode):
  newnode = Node(
                      parent_node=None,
                      state=insertnode,
                      action=None,
                      depth=0)
  fifo = deque([newnode])
  count = 0
  Level = []
  collectionoflist = []
  while (True):
    if not fifo:
      return None
    node = fifo.popleft()
    if(count == node.depth):
        collectionoflist.append(node.state)
    else:
        Level.append(list(collectionoflist))
        collectionoflist.clear()    
        collectionoflist.append(node.state)
        count = count + 1
    if(node.state.is_finalstate()):
        Level.append(list(collectionoflist))
    if node.state.is_finalstate():
      solution = node.extract_solution() 
    
      
      return solution, Level
    fifo.extend(node.recursion()) #Fukaune kaam node ko children lai

    


def main():
  insertnode = State(3,3,1)
  solution, Level = bfs_search(insertnode)
  count = 0
  print ("Name : Vaibhav Sapkota")
  print ("Roll No. 41")
  print ("\n")    
  print ("Solution Path:" )
  print ("\n")    
  for x in solution:
      print ("%s\n" % x)
  print ("\n") 
  print('TREE :\n')
  for i in Level:
          print("Depth",count,"-->",i)
          count = count + 1
          print("\n")
    


if __name__ == "__main__":
  main()
  
