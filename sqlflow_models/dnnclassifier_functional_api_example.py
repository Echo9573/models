import tensorflow as tf

def dnnclassifier_functional_model(feature_columns, field_metas, learning_rate=0.01):
    feature_layer_inputs = dict()
    for fmkey in field_metas:
        fm = field_metas[fmkey]
        feature_layer_inputs[fm["name"]] = tf.keras.Input(shape=(fm["shape"]), name=fm["name"], dtype=fm["dtype"])
    feature_layer = tf.keras.layers.DenseFeatures(feature_columns)
    feature_layer_outputs = feature_layer(feature_layer_inputs)

    x = tf.keras.layers.Dense(128, activation='relu')(feature_layer_outputs)
    x = tf.keras.layers.Dense(64, activation='relu')(x)
    pred = tf.keras.layers.Dense(1, activation='sigmoid')(x)
    return tf.keras.Model(inputs=[v for v in feature_layer_inputs.values()], outputs=pred)

def loss(output, labels):
    return tf.reduce_mean(tf.keras.losses.binary_crossentropy(labels, output))

# FIXME(typhoonzero): use the name loss once ElasticDL has updated.
def loss_new(y_true, y_pred):
    return tf.reduce_mean(tf.keras.losses.binary_crossentropy(y_true, y_pred))

def epochs():
    return 1

def optimizer(lr=0.1):
    return tf.optimizers.SGD(lr)

def prepare_prediction_column(self, prediction):
    """Return the class label of highest probability."""
    return prediction.argmax(axis=-1)
