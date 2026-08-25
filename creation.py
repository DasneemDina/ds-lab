{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNksgBl4lUwv72Amc3VZMVf",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/DasneemDina/ds-lab/blob/main/creation.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class Node:\n",
        "  def __init__(self, data):\n",
        "    self.data = data\n",
        "    self.next = None\n",
        "\n",
        "class LinkedList:\n",
        "  def __init__(self):\n",
        "    self.head = None\n",
        "\n",
        "  def push(self, new_data):\n",
        "    new_node = Node(new_data)\n",
        "    new_node.next = self.head\n",
        "    self.head = new_node\n",
        "\n",
        "  def insertafter(self, prev_node, new_data):\n",
        "    if prev_node is None:\n",
        "      print(\"The given previous node must be in the linked list.\")\n",
        "      return\n",
        "    new_node = Node(new_data)\n",
        "    new_node.next = prev_node.next\n",
        "    prev_node.next = new_node\n",
        "\n",
        "  def append(self, new_data):\n",
        "    new_node = Node(new_data)\n",
        "    if self.head is None:\n",
        "      self.head = new_node\n",
        "      return\n",
        "    last = self.head\n",
        "    while last.next:\n",
        "      last = last.next\n",
        "    last.next = new_node\n",
        "\n",
        "  def printlist(self):\n",
        "    temp = self.head\n",
        "    while temp:\n",
        "      print(temp.data)\n",
        "      temp = temp.next\n",
        "\n",
        "if __name__ == '__main__':\n",
        "  llist = LinkedList()\n",
        "  llist.append(6)\n",
        "  llist.push(7)\n",
        "  llist.push(1)\n",
        "  llist.append(4)\n",
        "  llist.insertafter(llist.head.next, 8)\n",
        "  print('Created linked list is:')\n",
        "  llist.printlist()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_FGEwdDrBve8",
        "outputId": "c5a1b837-db78-4515-bc05-48f60ceed0c4"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Created linked list is:\n",
            "1\n",
            "7\n",
            "8\n",
            "6\n",
            "4\n"
          ]
        }
      ]
    }
  ]
}