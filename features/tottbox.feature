Feature: tottbox
    A description of some basic landmarks of the tottbox environment.
    A sanity check.

    Scenario: Check the /vagrant mount
        Given the /vagrant folder
        When we list its contents
        Then we see the Vagrantfile

    Scenario: Check the network
        Given we execute ifconfig
        When we check the assigned IPs
        Then we see a 192.168.x.x address
