#Implementation of Kasaraju's Algorithm to compute the
#number of strongly connected components in a given graph

require_relative 'stack'

class SCC
  attr_accessor :adj_list, :current_finish_time, 
    :dfs_stack, :finish_time_list, :leader_node_list,
    :explored_list
  
  def initialize
    self.adj_list = []
    @current_finish_time = 0
    self.explored_list = Hash.new
    self.finish_time_list = Hash.new
    self.dfs_stack = Stack.new
    self.leader_node_list = Hash.new
  end
  
  def start
    #process G-reverse and note the finish times
    self.read_g 'reverse'
    p 'read reverse'
    self.DFS_loop_grev()
    p @current_finish_time
    
    self.adj_list = []
    self.explored_list = Hash.new
    self.dfs_stack = Stack.new
    
    #process G in the order of above finish times
    self.read_g 'normal'
    p 'read normal'
    self.DFS_loop_g()
#    p self.leader_node_list.keys[-1], self.leader_node_list.values[-1]
    
#    self.leader_node_list.sort_by { |key, value| value.length }.reverse[0..4]
    
  end
  
  def read_g whichway
    File.open('4input.txt','r').each_line do |line|
      line = line.chomp.split(/[\s\t]/).map { |x| x.to_i }
      
      if whichway == 'reverse'
        if self.adj_list[line[1]]
          edges = adj_list[line[1]]
          edges += [line[0]]
        else
          edges = [line[0]]
        end
        self.adj_list[line[1]] = edges
      
      else
        if self.adj_list[line[0]]
          edges = adj_list[line[0]]
          edges += [line[1]]
        else
          edges = [line[1]]
        end
        self.adj_list[line[0]] = edges
      end
    end
  end
  
  #iterate in the same order as finish time list keys
  def DFS_loop_g
    self.finish_time_list.sort.reverse.each { |time, node|
        next if self.adj_list[node].nil?
        @current_leader = node
        if !self.explored_list.has_key?(node) then n = Node.new(node); iDFS_g n; end
    }
  end
  
  #to keep track of finish times (topological ordering)
  def DFS_loop_grev
    self.adj_list().each_with_index { |val, i|
      self.adj_list[i] = [] if self.adj_list[i].nil?
      #call i-dfs if a node hasn't been explored yet
      if !self.explored_list.has_key?(i) then n = Node.new(i); iDFS_grev n; end
    }
  end
  
  def iDFS_g node
    self.explored_list[node.label] = node
    self.dfs_stack().push(node)
    self.leader_node_list[@current_leader] = [node.label]
    
    until self.dfs_stack.empty?
      top_guy = self.dfs_stack.peek
#      p top_guy
      
      l = self.adj_list[top_guy.label]
      #if top guy has no neighbors, pop him out
      if l.nil? or l.empty?
        self.dfs_stack.pop
      else
        self.adj_list[top_guy.label].each { |eachnode|
          if self.explored_list().has_key?(eachnode)
#            has_unvisited_node = false
#            self.adj_list[top_guy.label].each { |i| has_unvisited_node = true unless self.explored_list().has_key?(i) }
#            
#            if has_unvisited_node then next
            if !self.adj_list[top_guy.label].empty?
              next
            else 
              self.dfs_stack.pop
              break if dfs_stack.empty? 
            end

          else
            n = Node.new(eachnode)
            self.dfs_stack.push(n)
            self.explored_list[n.label()] = n
            self.adj_list[top_guy.label].delete(eachnode)
            self.leader_node_list[@current_leader] += [n.label]
            break
          end
        }
      end
    end
    
  end
  
  def iDFS_grev node
    self.explored_list[node.label] = node
    self.dfs_stack().push(node)
    
    until self.dfs_stack.empty?
      top_guy = self.dfs_stack.peek
      
      l = self.adj_list[top_guy.label]
      #if top guy has no neighbors, pop him out
      if l.nil? or l.empty?
        #update current finish time and the finish time list
        @current_finish_time += 1
        n = self.dfs_stack.pop
        self.finish_time_list[@current_finish_time] = n.label
      else
        l.each { |eachnode|
          #if the node has been explored, check if there are other
          #unexplored neighbors for top guy
          #if yes, continue with next neighbor. 
          #else, start popping and update finish times.
          if self.explored_list().has_key?(eachnode)
#            has_unvisited_node = false
#            self.adj_list[top_guy.label].each { |i| has_unvisited_node = true unless self.explored_list().has_key?(i) }
#            
#            if has_unvisited_node
#              next
            if !self.adj_list[top_guy.label].empty?
              next
            else 
              #update current finish time and the finish time list
              @current_finish_time += 1
              n = self.dfs_stack.pop
              self.finish_time_list[@current_finish_time] = n.label
              break if dfs_stack.empty?
            end
          #if the node is unexplored, then create a new node object,
          #mark it as explored and push into stack
          else
            n = Node.new(eachnode)
            self.dfs_stack.push(n)
            self.explored_list[n.label()] = n
            self.adj_list[top_guy.label].delete(eachnode)
            break
          end
        }
      end
    end
  end
  
end
    
class Node
  attr_accessor :label
  
  def initialize(key)
    self.label=(key)
  end
  
end

if __FILE__ == $0
  SCC.new.start
end