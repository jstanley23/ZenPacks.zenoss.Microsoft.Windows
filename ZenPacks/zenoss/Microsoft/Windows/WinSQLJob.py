##############################################################################
#
# Copyright (C) Zenoss, Inc. 2013, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

from Globals import InitializeClass

from Products.ZenModel.OSComponent import OSComponent
from Products.ZenRelations.RelSchema import ToOne, ToManyCont


class WinSQLJob(OSComponent):
    '''
    Model class for MSSQLJobs.
    '''
    meta_type = portal_type = 'WinSQLJob'

    instancename = None
    jobid = None
    enabled = None
    description = None
    username = None
    datecreated = None
    cluster_node_server = None
    usermonitor = False

    _properties = OSComponent._properties + (
        {'id': 'instancename', 'label': 'Instance Name', 'type': 'string'},
        {'id': 'jobid', 'label': 'Job ID', 'type': 'string'},
        {'id': 'enabled', 'label': 'Enabled', 'type': 'string'},
        {'id': 'description', 'label': 'Description', 'type': 'string'},
        {'id': 'username', 'label': 'User', 'type': 'string'},
        {'id': 'datecreated', 'label': 'Date Created', 'type': 'string'},
        {'id': 'cluster_node_server', 'label': 'Cluster Node Server', 'type': 'string'},
        {'id': 'usermonitor', 'label': 'User Selected Monitor State',
            'type': 'boolean'},
        )

    _relations = OSComponent._relations + (
        ("winsqlinstance", ToOne(ToManyCont,
            "ZenPacks.zenoss.Microsoft.Windows.WinSQLInstance",
            "jobs")),
    )

    def getRRDTemplateName(self):
        return 'WinSQLJob'

    def monitored(self):
        """Return True if this service should be monitored. False otherwise."""

        # 1 - Check to see if the user has manually set monitor status
        if self.usermonitor is True:
            return self.monitor

        # 2 - return status of enabled. do not monitor disabled jobs
        return self.enabled == 'Yes'

InitializeClass(WinSQLJob)
