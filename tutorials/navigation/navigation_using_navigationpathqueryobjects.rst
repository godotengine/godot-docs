.. _doc_navigation_using_navigationpathqueryobjects:

Using NavigationPathQueryObjects
================================

``NavigationPathQueryObjects`` can be used together with ``NavigationServer.query_path()``
to obtain a heavily **customized** navigation path including optional **meta data** about the path.

This requires more setup compared to obtaining a normal NavigationPath but lets you tailor
the pathfinding and provided path data to the different needs of a project.

NavigationPathQueryObjects consist of a pair of objects, a ``NavigationPathQueryParameters`` object holding the customization options
for the query and a ``NavigationPathQueryResult`` that receives (regular) updates with the resulting path and meta data from the query.

2D and 3D versions of ``NavigationPathQueryParameters`` are available as
:ref:`NavigationPathQueryParameters2D<class_NavigationPathQueryParameters2D>` and
:ref:`NavigationPathQueryParameters3D<class_NavigationPathQueryParameters3D>` respectively.

2D and 3D versions of ``NavigationPathQueryResult`` are available as
:ref:`NavigationPathQuerResult2D<class_NavigationPathQueryResult2D>` and
:ref:`NavigationPathQueryResult3D<class_NavigationPathQueryResult3D>` respectively.

Both parameters and result are used as a pair with the ``NavigationServer.query_path()`` function.

For the available customization options and their use see the class doc of the parameters.

While not a strict requirement, both objects are intended to be created once in advance, stored in a
persistent variable for the agent and reused for every followup path query with updated parameters.
This reuse avoids performance implications from frequent object creation if a project
has a large quantity of simultaneous agents that regularly update their paths.

.. tabs::
 .. code-tab:: gdscript GDScript

    # prepare query objects
    var query_parameters = NavigationPathQueryParameters2D.new()
    var query_result  = NavigationPathQueryResult2D.new()

    # update parameters object
    query_parameters.map = get_world_2d().get_navigation_map()
    query_parameters.start_position = agent2d_current_global_position
    query_parameters.target_position = agent2d_target_global_position

    # update result object
    NavigationServer2D.query_path(query_parameters, query_result)
    var path: PackedVector2Array = query_result.get_path()

.. tabs::
 .. code-tab:: gdscript GDScript

    # prepare query objects
    var query_parameters = NavigationPathQueryParameters3D.new()
    var query_result  = NavigationPathQueryResult3D.new()

    # update parameters object
    query_parameters.map = get_world_3d().get_navigation_map()
    query_parameters.start_position = agent3d_current_global_position
    query_parameters.target_position = agent3d_target_global_position

    # update result object
    NavigationServer3D.query_path(query_parameters, query_result)
    var path: PackedVector3Array = query_result.get_path()
