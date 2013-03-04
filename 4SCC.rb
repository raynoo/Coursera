#Implementation of Kosaraju's Algorithm to compute the
#number of strongly connected components in a given graph

require_relative 'stack'
require 'set'

class SCC
  attr_accessor :adj_list, :explored_list,
    :dfs_stack, :finish_time_list, :leader_node_list
  
  def initialize
    @explored_list = Set.new
    @dfs_stack = Stack.new
    @finish_time_list = Array.new
    @leader_node_list = Hash.new
  end
  
  def start
    #process G-reverse and note the finish times
    self.read_input 'reverse'
    self.DFS_loop_grev
#    self.finish_time_list.each { |i| p i }
    
    #clear the explored list and stack
    #stack should be empty by now but just in case
    self.explored_list = Set.new
    self.dfs_stack = Stack.new
    
    #process G in the order of above finish times
    self.read_input 'normal'
#    self.read_times()
    self.DFS_loop_g()
    
    #print out top 5 SCC's sizes
    @leader_node_list.sort_by { |key, value| 
      value
    }.reverse[0..4].each{ |leader, nodes| 
      puts 'SCC size: ' + nodes.to_s
    }
  end
  
  def read_input whichway
    @adj_list = []
    
    @num_of_nodes = 875714 #n as in range 1 to n (not 0 to n)
    File.open('4input.txt','r').each_line do |line|
      line = line.chomp.split(/[\s\t]/).map { |x| x.to_i }
      
      #graph G-Reverse
      if whichway == 'reverse'
        if @adj_list[line[1]]
          @adj_list[line[1]] += [line[0]]
        else
          @adj_list[line[1]] = [line[0]]
        end
      #graph G
      else
        if @adj_list[line[0]]
          @adj_list[line[0]] += [line[1]]
        else
          @adj_list[line[0]] = [line[1]]
        end
      end
    end
  end
  
  #to debug finish time list stored in file
  def read_times
    @finish_time_list = []
    File.open('finlist.txt','r').each_line do |line|
      @finish_time_list.push line.chomp.to_i
    end
  end
  
  #traverse g-reverse by dfs, from n to 1, and calculate their finish times
  def DFS_loop_grev
    @current_finish_time = 0
    @num_of_nodes.downto(1) { |i| iDFS_grev i unless @explored_list.include?(i) }
    
  end
  
  #iterative dfs for g-reverse
  def iDFS_grev node
    @explored_list.add node
    @dfs_stack.push node
    
    until @dfs_stack.empty?
      top_guy = @dfs_stack.peek
      l = @adj_list[top_guy]
      
      #if top guy has no neighbors, pop him out
      if l.nil? or l.empty?
        #update current finish time and the finish time list
        @current_finish_time += 1
        @finish_time_list[@current_finish_time] = @dfs_stack.pop
      else
        has_unvisited_node = false
        l.each { |eachnode|
          #if the node is unexplored, then mark it as explored
          #and push into stack
          if !@explored_list.include?(eachnode)
            @explored_list.add eachnode
            @dfs_stack.push eachnode
            has_unvisited_node = true
            break
          end
        }
        #if top guy has no more unexplored neighbors
        unless has_unvisited_node
          @current_finish_time += 1
          @finish_time_list[@current_finish_time] = @dfs_stack.pop
          break if dfs_stack.empty?
        end
      end
    end
  end
  
  #iterate in the same order as finish time list keys
  def DFS_loop_g
    @finish_time_list.reverse.each { |node|
#    @time.reverse.each { |node|
      next if node.nil?
      @current_leader = node
      iDFS_g node unless @explored_list.include?(node)
    }
  end
  
  #iterative dfs for g
  def iDFS_g node
    @explored_list.add node
    @dfs_stack.push node
    
    until @dfs_stack.empty?
      top_guy = @dfs_stack.pop
      
      if @leader_node_list.has_key? @current_leader
        @leader_node_list[@current_leader] += 1
      else
        @leader_node_list[@current_leader] = 1
      end
      
      l = @adj_list[top_guy]
      if l.nil? or l.empty?
        
      else
        l.each { |eachnode|
          if @explored_list.include?(eachnode)
            
          else
            @dfs_stack.push eachnode
            @explored_list.add eachnode
          end
        }
      end
    end
    
  end
  
end

if __FILE__ == $0
  SCC.new.start
end