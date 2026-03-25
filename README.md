# Example ROS2 Software Packages

[![CI](https://github.com/calebjakemossey/assignment_example_ros_pkg/actions/workflows/ci.yaml/badge.svg)](https://github.com/calebjakemossey/assignment_example_ros_pkg/actions/workflows/ci.yaml)

ROS2 workspace containing interface definitions and nodes that demonstrate topic, service, and action communication patterns.

> **Note**: This project targets **ROS2 Humble** (LTS, supported until May 2027). The original starter code referenced Iron, which reached end-of-life in December 2024.

## Architecture

```mermaid
graph TB
    subgraph "This Repository"
        msgs[example_package_msgs<br/>Service & Action definitions]
        ros[example_package_ros<br/>ROS2 nodes]
    end

    subgraph "External Dependency"
        pkg[assignment_example_pkg<br/>ROS-independent Example class]
    end

    ros --> msgs
    ros --> pkg

    style msgs fill:#e1f5fe
    style ros fill:#e1f5fe
    style pkg fill:#fff3e0
```

## Packages

| Package | Description |
|---------|-------------|
| `example_package_msgs` | Custom service (`Example.srv`) and action (`Example.action`) interface definitions |
| `example_package_ros` | ROS2 nodes using `Example` class from `assignment_example_pkg` |

## Getting Started

See [CONTRIBUTING.md](CONTRIBUTING.md) for workspace setup, building, and testing instructions.

Refer to [example_package_ros/README.md](example_package_ros/README.md) for detailed usage of the ROS2 nodes.
