#!/bin/bash

# Function to install or update AWS CLI
install_update_awscli() {
    # Remove existing AWS CLI if present
    if command -v aws &>/dev/null; then
        echo "Removing existing AWS CLI..."
        sudo yum remove awscli -y
    fi

    # Install or update AWS CLI
    echo "Installing or updating AWS CLI..."
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip -o awscliv2.zip
    sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update
    echo "AWS CLI installation or update completed."

    # Clean up leftover files
    echo "Cleaning up..."
    rm -rf awscliv2.zip aws
    echo "Cleanup completed."
}

# Function to check OS version and install/update dependencies
check_install_dependencies() {
    # Check if yum package manager is available
    if command -v yum &>/dev/null; then
        # Install dependencies for yum-based distributions
        echo "Installing dependencies for yum-based distributions..."
        sudo yum install -y unzip
    elif command -v apt &>/dev/null; then
        # Install dependencies for apt-based distributions
        echo "Installing dependencies for apt-based distributions..."
        sudo apt update
        sudo apt install -y unzip
    else
        echo "Unsupported package manager. Please install the dependencies manually."
        exit 1
    fi
}

# Main script
echo "Checking OS version and installing/updating dependencies..."
check_install_dependencies

echo "Installing or updating AWS CLI..."
install_update_awscli

echo "Script execution completed."

