# Copyright 2017 Catalyst IT Limited
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from qinlingclient.common import base


class FunctionExecution(base.Resource):
    pass


class ExecutionManager(base.Manager):
    resource_class = FunctionExecution

    def list(self, function_id=None, **kwargs):
        q_params = ''
        if function_id:
            q_params += 'function_id=%s' % function_id

        url = "/v1/executions"
        if q_params:
            url += '?%s' % q_params

        return self._list(url, response_key='executions')

    def create(self, function, sync=True, input={}):
        data = {'function_id': function, 'sync': sync, 'input': input}
        return self._create('/v1/executions', data)

    def delete(self, id):
        self._delete('/v1/executions/%s' % id)

    def get(self, id):
        return self._get('/v1/executions/%s' % id)

    def get_log(self, id):
        return self._get('/v1/executions/%s/log' % id, return_raw=True)
