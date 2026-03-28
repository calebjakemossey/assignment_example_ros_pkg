# Example ROS2 Software Packages

[![CI](https://github.com/calebjakemossey/assignment_example_ros_pkg/actions/workflows/ci.yaml/badge.svg)](https://github.com/calebjakemossey/assignment_example_ros_pkg/actions/workflows/ci.yaml)

ROS2 workspace containing interface definitions and nodes that demonstrate topic, service, and action communication patterns.

> **Note**: This project targets **ROS2 Humble** (LTS, supported until May 2027). The original starter code referenced Iron, which reached end-of-life in December 2024.

## Architecture

```mermaid
%%{init: {'theme': 'dark', 'flowchart': {'curve': 'linear'}}}%%
graph TB
    classDef primary fill:#2d5986,stroke:#4a90d9,stroke-width:1px,color:#e0e0e0,rx:8,ry:8
    classDef secondary fill:#1a3a5c,stroke:#3d7ab5,stroke-width:1px,color:#e0e0e0,rx:8,ry:8
    classDef accent fill:#2d7d46,stroke:#4caf50,stroke-width:1px,color:#e0e0e0,rx:8,ry:8

    subgraph "This Repository"
        msgs[example_package_msgs<br/>Service & Action definitions]:::primary
        ros[example_package_ros<br/>ROS2 nodes]:::primary
    end

    subgraph "External Dependency"
        pkg[assignment_example_pkg<br/>ROS-independent Example class]:::accent
    end

    ros --> msgs
    ros --> pkg
```

## Packages

| Package | Description |
|---------|-------------|
| `example_package_msgs` | Custom service (`Example.srv`) and action (`Example.action`) interface definitions |
| `example_package_ros` | ROS2 nodes using `Example` class from `assignment_example_pkg` |

## Getting Started

See [CONTRIBUTING.md](CONTRIBUTING.md) for workspace setup, building, and testing instructions.

Refer to [example_package_ros/README.md](example_package_ros/README.md) for detailed usage of the ROS2 nodes.
