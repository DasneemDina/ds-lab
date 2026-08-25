{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOQkg/OpWGzYc8Idf8JShSl",
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
        "<a href=\"https://colab.research.google.com/github/DasneemDina/ds-lab/blob/main/deletion.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class Node:\n",
        "  def __init__(self, data=None):\n",
        "    self.data = data\n",
        "    self.next = None\n",
        "\n",
        "class SLinkedList:\n",
        "  def __init__(self):\n",
        "    self.head = None\n",
        "\n",
        "  def at_beginning(self, data_in):\n",
        "    new_node = Node(data_in)\n",
        "    new_node.next = self.head\n",
        "    self.head = new_node\n",
        "\n",
        "  def remove_node(self, removekey):\n",
        "    head_val = self.head\n",
        "\n",
        "    # Case 1: Head node itself holds the key to be deleted\n",
        "    if head_val is not None and head_val.data == removekey:\n",
        "      self.head = head_val.next\n",
        "      head_val = None # Free memory (though Python's GC handles this)\n",
        "      return\n",
        "\n",
        "    # Search for the key to be deleted, keep track of the previous node\n",
        "    prev = None\n",
        "    while head_val is not None and head_val.data != removekey:\n",
        "      prev = head_val\n",
        "      head_val = head_val.next\n",
        "\n",
        "    # If key was not present in linked list\n",
        "    if head_val is None:\n",
        "      return\n",
        "\n",
        "    # Unlink the node from linked list\n",
        "    prev.next = head_val.next\n",
        "    head_val = None\n",
        "\n",
        "  def print_list(self):\n",
        "    print_val = self.head\n",
        "    while print_val:\n",
        "      print(print_val.data)\n",
        "      print_val = print_val.next\n",
        "\n",
        "if __name__ == '__main__':\n",
        "  llist = SLinkedList()\n",
        "  llist.at_beginning(\"Mon\")\n",
        "  llist.at_beginning(\"Tue\")\n",
        "  llist.at_beginning(\"Wed\")\n",
        "  llist.at_beginning(\"Thu\")\n",
        "\n",
        "  # The list is now: Thu -> Wed -> Tue -> Mon\n",
        "  llist.remove_node(\"Tue\")\n",
        "\n",
        "  print('Created linked list is:')\n",
        "  llist.print_list()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yFJOoWi0EYgL",
        "outputId": "e2ec8cb2-70f4-4f67-96b7-1a4e4ca6d7cd"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Created linked list is:\n",
            "Thu\n",
            "Wed\n",
            "Mon\n"
          ]
        }
      ]
    }
  ]
}