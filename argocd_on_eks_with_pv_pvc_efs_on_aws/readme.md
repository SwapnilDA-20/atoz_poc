

after installing argocd how to attach efs as pv for argocd 

in volumemounts section add below line mountpath and name 

          readOnlyRootFilesystem: true
          runAsNonRoot: true
          seccompProfile:
            type: RuntimeDefault
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        volumeMounts:
        - mountPath: /argocd
          name: argocd-data

