# Contributing

## Prerequisites

- [ROS2 Humble](https://docs.ros.org/en/humble/Installation.html) (LTS, supported until May 2027)
- [colcon](https://colcon.readthedocs.io/) build tool
- [vcstool](https://github.com/dirk-thomas/vcstool) for workspace dependency management
- Python 3.10+

## Workspace Setup

```bash
# Create a ROS2 workspace
mkdir -p ros_ws/src
cd ros_ws

# Clone this repository into src/
git clone git@github.com:calebjakemossey/assignment_example_ros_pkg.git src/assignment_example_ros_pkg

# Import pinned dependencies (assignment_example_pkg)
vcs import src < src/assignment_example_ros_pkg/workspace.repos

# Install rosdep dependencies
source /opt/ros/humble/setup.bash
rosdep install --from-paths src --ignore-src -r -y

# Build the workspace
colcon build --symlink-install

# Source the workspace
source install/local_setup.bash
```

## Running Tests

```bash
# Run tests for all packages
colcon test
colcon test-result --verbose

# Run tests for a specific package
colcon test --packages-select example_package_ros
colcon test-result --verbose
```

## Linting

The CI pipeline runs ament linters automatically. To run them locally:

```bash
ament_flake8
ament_pep257
ament_xmllint
```

## Branching Convention

- Feature branches: `feat/<description>`
- Bug fixes: `fix/<description>`
- Documentation: `docs/<description>`

Branch from `main` and open a PR back to `main`.

## Pull Request Requirements

1. All CI checks must pass
2. Fill in the PR template with a summary and change list
3. Ensure `colcon build` and `colcon test` succeed locally before pushing

## Note on ROS2 Distribution

This project targets **ROS2 Humble** (LTS). The original starter code referenced ROS2 Iron, which reached end-of-life in December 2024. All documentation and CI have been updated to use Humble.
