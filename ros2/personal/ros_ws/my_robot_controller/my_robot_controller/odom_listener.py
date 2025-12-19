#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class SquareMove(Node):
    def __init__(self):
        super().__init__('odom_listener')
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        
        self.linear_speed = 0.2  # м/с
        self.angular_speed = 0.5  # рад/с
        self.side_duration = 2.0  # секунд на сторону
        self.turn_duration = 3.2  # секунд на поворот
        
        self.state = 'forward'
        self.start_time = time.time()
        self.side_count = 0
        
        self.get_logger().info('Square Move Node started')
        
    def timer_callback(self):
        current_time = time.time()
        twist = Twist()
        
        if self.side_count >= 4:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            self.cmd_vel_pub.publish(twist)
            self.get_logger().info('Square completed')
            rclpy.shutdown()
            return
            
        if self.state == 'forward':
            if current_time - self.start_time < self.side_duration:
                twist.linear.x = self.linear_speed
                twist.angular.z = 0.0
            else:
                self.state = 'turn'
                self.start_time = current_time
                self.get_logger().info(f'Turning {self.side_count + 1}')
                
        elif self.state == 'turn':
            if current_time - self.start_time < self.turn_duration:
                twist.linear.x = 0.0
                twist.angular.z = self.angular_speed
            else:
                self.state = 'forward'
                self.start_time = current_time
                self.side_count += 1
                self.get_logger().info(f'Side {self.side_count} completed')
                
        self.cmd_vel_pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = SquareMove()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()