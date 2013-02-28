#Implementation of Kasaraju's Algorithm to compute the
#number of strongly connected components in a given graph

require_relative 'stack'

class SCC
  attr_accessor :adj_list, :current_finish_time, #:current_leader, 
    :dfs_stack, :finish_time_list, :leader_node_list,
    :explored_list
  
  def initialize
    self.adj_list = []
    self.current_finish_time = 0
    self.explored_list = Hash.new
    self.finish_time_list = Hash.new
    self.dfs_stack = Stack.new
  end
  
  def start
    self.read_g()
    self.DFS_loop()
  end
  
  def read_g
    File.open('4test_4.txt','r').each_line do |line|
      line = line.chomp.split(/[\s\t]/).map { |x| x.to_i }
      
      if self.adj_list[line[0]] then
        edges = adj_list[line[0]]
        edges += [line[1]]
      else
        edges = [line[1]]
      end
      self.adj_list[line[0]] = edges
    end
  end
  
  def read_grev
    File.open('4test_4.txt','r').each_line do |line|
      line = line.chomp.split(/[\s\t]/).map { |x| x.to_i }
      
      if self.adj_list[line[1]] then
        edges = adj_list[line[1]]
        edges += [line[0]]
      else
        edges = [line[0]]
      end
      self.adj_list[line[1]] = edges
    end
  end
  
  def DFS_loop
    self.adj_list().each_with_index { |val, i|
      node = i + 1
      @current_leader = node
      if self.explored_list.include?(node)
        n = self.explored_list[node]
      else
        n = Node.new(node)
      end
      DFS n unless n.explored
    }
    p self.finish_time_list()
  end
  
  def DFS node
    node.explored = true
    self.explored_list[node.label] = node
    node.leader = @current_leader
    
    if self.adj_list[node.label]
      self.adj_list[node.label].each { |j| DFS Node.new(j) unless self.explored_list().include?(j) }
    end
    self.current_finish_time = self.current_finish_time + 1
    self.finish_time_list[self.current_finish_time] = node #list to track finishing times
    
  end
  
  def iDFS node
    node.explored = true
    self.dfs_stack().push(node)
    node.leader = @current_leader
    
    #iterate until stack is empty
    until self.dfs_stack.empty?
      #peek (at) node on stack
      top_guy = self.dfs_stack.peek 
      
      #iterate over adjacency list of top_guy
      ##if the node present in adjacency list, and its unexplored,
      ##then mark it explored and push into stack
      self.adj_list[top_guy.label].each { |n| 
        if self.adj_list[n] and !n.explored
          n.explored = true
          self.dfs_stack.push(n)
        
        elsif !self.adj_list[n]
          
          self.dfs_stack.pop
        end 
      }
      
    end
    
  end
  
  
end
    
class Node
  attr_accessor :label, :explored, :leader
  
  def initialize(key)
    self.label=(key)
    self.explored=(false)
  end
  
end

if __FILE__ == $0
  SCC.new.start
end