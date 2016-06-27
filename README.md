# vk-common-groups
Get common groups on vk.com

This .py file contains a function <b>get_common_groups(group_id, number_of_common_groups, token)</b>.

* <b>group_id</b> - id of the group, among which members you want to search for common groups
* <b>number_of_common_groups</b> - how many common groups to show
* <b>token</b> - vk.com access token

This function solve the simple task of deciding what else have in common the members of a certain vk group/public. 
For example, if we consider a public with data science topics, then we check if in the top n there are other publics with the same topic.
Kind of hypotheses checking.

Example of its work can be found in jupyter notebook file.
