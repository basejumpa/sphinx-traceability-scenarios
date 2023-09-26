Scenario 1
##########

Requirement Specification
*************************

.. item:: REQ_0001

    Content of REQ_0001

.. item:: REQ_0002

    Content of REQ_0002

.. item:: REQ_0003

    Content of REQ_0003

Design Specification
********************

.. item:: DESIGN_0001
    :fulfills: REQ_0001 REQ_0002

    Content of DESIGN_0001

.. ifconfig:: True

    Some text before the item.

    .. item:: DESIGN_0002
        :fulfills: REQ_0002

        Content of DESIGN_0002

    Some text after the item.

.. ifconfig:: False

    Some text before the item.

    .. item:: DESIGN_0003
        :fulfills: REQ_0003

        Content of DESIGN_0003

    Some text after the item.

Traceability
************

.. item-matrix:: 
    :source: REQ
    :target: DESIGN
    :stats:
