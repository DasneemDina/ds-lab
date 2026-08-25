{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPaLpXdLxPTpDmoTUmREykQ",
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
        "<a href=\"https://colab.research.google.com/github/DasneemDina/ds-lab/blob/main/traversal.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class node:\n",
        "  def __init__(self, data):\n",
        "    self.data = data\n",
        "    self.next = None\n",
        "\n",
        "class LinkedList:\n",
        "  def __init__(self):\n",
        "    self.head = None\n",
        "\n",
        "  def printlist(self):\n",
        "    temp = self.head\n",
        "    while(temp):\n",
        "      print(temp.data)\n",
        "      temp = temp.next\n",
        "\n",
        "if __name__ == '__main__':\n",
        "  llist = LinkedList()\n",
        "  llist.head = node(1)\n",
        "  second = node(2)\n",
        "  third = node(3)\n",
        "  llist.head.next = second\n",
        "  second.next = third\n",
        "  llist.printlist()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GVCYHsJ_G70D",
        "outputId": "297c16d7-950f-42f2-9f33-82f1687ae073"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n"
          ]
        }
      ]
    }
  ]
}